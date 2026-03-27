"""
ServiceDesk Plus API Client (On-Premise)
"""

import aiohttp
import sys
from typing import Dict, Any, Optional
from config import Config


class ServiceDeskPlusClient:
    """Client for interacting with ServiceDesk Plus On-Premise API v3"""

    def __init__(self):
        self.base_url = Config.SDP_BASE_URL.rstrip("/")
        self.api_key = Config.SDP_API_KEY
        self.session: Optional[aiohttp.ClientSession] = None
        self._auth_valid = False

    async def __aenter__(self):
        await self.authenticate()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def authenticate(self) -> bool:
        if not self.session:
            timeout = aiohttp.ClientTimeout(total=Config.REQUEST_TIMEOUT)
            self.session = aiohttp.ClientSession(timeout=timeout)

        if self._auth_valid:
            return True

        config_validation = Config.validate_config()
        if not config_validation["valid"]:
            raise ValueError(f"Configuration issues: {config_validation['issues']}")

        try:
            import json

            headers = {"authtoken": self.api_key, "Accept": "application/json"}
            params = {"input_data": json.dumps({"list_info": {"row_count": 1}})}
            async with self.session.get(
                f"{self.base_url}{Config.API_ENDPOINTS['tickets']}",
                headers=headers,
                params=params,
            ) as response:
                if response.status == 200:
                    self._auth_valid = True
                    return True
                else:
                    print(f"Authentication failed: {response.status} - {await response.text()}", file=sys.stderr)
                    return False
        except Exception as e:
            print(f"Authentication error: {e}", file=sys.stderr)
            return False

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        import json as _json

        if not await self.authenticate():
            raise Exception("Authentication failed")

        url = f"{self.base_url}{endpoint}"
        headers = {
            "authtoken": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        query_params: Dict[str, str] = {}

        if params:
            input_data: Dict[str, Any] = {}
            list_info: Dict[str, Any] = {}
            search_criteria = []

            for key, value in params.items():
                if key == "limit":
                    list_info["row_count"] = value
                elif key == "start_at":
                    list_info["start_index"] = value
                elif key in ("status", "priority", "requester"):
                    search_criteria.append({
                        "field": key if key != "requester" else "requester.name",
                        "condition": "is",
                        "value": value,
                    })
                elif key == "search_criteria":
                    search_criteria.extend(value)
                else:
                    input_data[key] = value

            if list_info:
                input_data["list_info"] = list_info
            if search_criteria:
                input_data["list_info"] = input_data.get("list_info", {})
                input_data["list_info"]["search_criteria"] = search_criteria

            if input_data:
                query_params["input_data"] = _json.dumps(input_data)

        request_data = None
        if json_data and method.upper() in ("POST", "PUT"):
            request_data = {"input_data": _json.dumps(json_data)}

        try:
            async with self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=query_params,
                data=request_data,
            ) as response:
                if response.status in [200, 201]:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"API request failed: {response.status} - {error_text}")
        except Exception as e:
            raise Exception(f"Request failed: {e}")

    # ==================== TICKETS ====================

    async def get_tickets(
        self,
        limit: int = Config.DEFAULT_LIMIT,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        requester: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": min(limit, Config.MAX_LIMIT)}
        if status:
            params["status"] = status
        if priority:
            params["priority"] = priority
        if requester:
            params["requester"] = requester
        return await self._make_request("GET", Config.API_ENDPOINTS["tickets"], params=params)

    async def get_ticket(self, ticket_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{ticket_id}")

    async def search_tickets(self, query: str, limit: int = Config.DEFAULT_LIMIT) -> Dict[str, Any]:
        params = {
            "limit": min(limit, Config.MAX_LIMIT),
            "search_criteria": [{"field": "subject", "condition": "contains", "value": query}],
        }
        return await self._make_request("GET", Config.API_ENDPOINTS["tickets"], params=params)

    async def get_ticket_comments(self, ticket_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{ticket_id}/notes")

    async def get_ticket_conversations(self, ticket_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{ticket_id}/conversations")

    async def get_request_tasks(self, request_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{request_id}/tasks")

    async def get_request_worklog(self, request_id: str, limit: int = 50) -> Dict[str, Any]:
        params = {"limit": min(limit, 1000)}
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{request_id}/worklogs", params=params)

    async def get_request_attachments(self, request_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{request_id}/attachments")

    async def get_request_notifications(self, request_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['tickets']}/{request_id}/notifications")

    # ==================== USERS ====================

    async def get_users(self, limit: int = Config.DEFAULT_LIMIT) -> Dict[str, Any]:
        params = {"limit": min(limit, Config.MAX_LIMIT)}
        return await self._make_request("GET", Config.API_ENDPOINTS["users"], params=params)

    async def get_user(self, user_id: str) -> Dict[str, Any]:
        return await self._make_request("GET", f"{Config.API_ENDPOINTS['users']}/{user_id}")
