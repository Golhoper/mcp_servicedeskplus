"""
Configuration for ServiceDesk Plus MCP Server (On-Premise)
"""

import os
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

# Search order: current directory → ~/.config/servicedeskplus-mcp/.env
_config_dir = Path.home() / ".config" / "servicedeskplus-mcp"
load_dotenv(_config_dir / ".env")
load_dotenv(override=False)  # current directory, won't override already-set values


class Config:
    SDP_BASE_URL = os.getenv("SDP_BASE_URL", "")
    SDP_API_KEY = os.getenv("SDP_API_KEY", "")

    API_ENDPOINTS = {
        "tickets": "/api/v3/requests",
        "users": "/api/v3/users",
    }

    DEFAULT_LIMIT = 50
    MAX_LIMIT = 1000
    REQUEST_TIMEOUT = 30

    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        issues = []
        if not cls.SDP_BASE_URL:
            issues.append("SDP_BASE_URL is not set")
        if not cls.SDP_API_KEY:
            issues.append("SDP_API_KEY is not set")
        return {"valid": len(issues) == 0, "issues": issues}
