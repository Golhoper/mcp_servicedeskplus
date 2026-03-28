import asyncio
import json
from typing import Any, Dict
from dotenv import load_dotenv

from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolResult,
    ListToolsResult,
    Tool,
    TextContent,
)

from sdp_client import ServiceDeskPlusClient
from config import Config

# Load environment variables
load_dotenv()

# Create MCP server
server = Server("servicedesk-plus")


@server.list_tools()
async def handle_list_tools() -> ListToolsResult:
    """List all available tools"""
    tools = [
        # ==================== TICKET MANAGEMENT ====================
        Tool(
            name="list_tickets",
            description="List tickets from ServiceDesk Plus with optional filters",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "description": "Maximum number of tickets (default: 50, max: 1000)",                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by ticket status",
                        "enum": ["open", "pending", "resolved", "closed", "cancelled", "on_hold"],
                    },
                    "priority": {
                        "type": "string",
                        "description": "Filter by priority level",
                        "enum": ["low", "medium", "high", "critical"],
                    },
                    "requester": {
                        "type": "string",
                        "description": "Filter by requester (email or ID)",
                    },
                },
            },
        ),
        Tool(
            name="get_ticket",
            description="Get detailed information of a ticket by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "string",
                        "description": "ID of the ticket to retrieve",
                    }
                },
                "required": ["ticket_id"],
            },
        ),
        Tool(
            name="search_tickets",
            description="Search tickets by keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search keyword",
                    },
                    "limit": {
                        "description": "Maximum number of results (default: 50, max: 1000)",                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="get_ticket_comments",
            description="Get list of comments for a ticket",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "string",
                        "description": "ID of the ticket",
                    }
                },
                "required": ["ticket_id"],
            },
        ),
        Tool(
            name="get_ticket_conversations",
            description="Get conversations (email replies) for a ticket",
            inputSchema={
                "type": "object",
                "properties": {
                    "ticket_id": {
                        "type": "string",
                        "description": "ID of the ticket",
                    }
                },
                "required": ["ticket_id"],
            },
        ),
        Tool(
            name="get_request_tasks",
            description="Get tasks associated with a request",
            inputSchema={
                "type": "object",
                "properties": {
                    "request_id": {
                        "type": "string",
                        "description": "ID of the request",
                    }
                },
                "required": ["request_id"],
            },
        ),
        Tool(
            name="get_request_worklog",
            description="Get worklog entries for a request",
            inputSchema={
                "type": "object",
                "properties": {
                    "request_id": {
                        "type": "string",
                        "description": "ID of the request",
                    },
                    "limit": {
                        "description": "Maximum number of records (default: 50, max: 1000)",                    },
                },
                "required": ["request_id"],
            },
        ),
        Tool(
            name="get_request_attachments",
            description="Get list of attachments for a request",
            inputSchema={
                "type": "object",
                "properties": {
                    "request_id": {
                        "type": "string",
                        "description": "ID of the request",
                    }
                },
                "required": ["request_id"],
            },
        ),
        Tool(
            name="get_request_notifications",
            description="Get list of notifications sent for a request",
            inputSchema={
                "type": "object",
                "properties": {
                    "request_id": {
                        "type": "string",
                        "description": "ID of the request",
                    }
                },
                "required": ["request_id"],
            },
        ),

        # ==================== USER MANAGEMENT ====================
        Tool(
            name="list_users",
            description="List users from ServiceDesk Plus",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "description": "Maximum number of users (default: 50, max: 1000)",                    }
                },
            },
        ),
        Tool(
            name="get_user",
            description="Get detailed information of a user",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "ID of the user to retrieve",
                    }
                },
                "required": ["user_id"],
            },
        ),
    ]

    return ListToolsResult(tools=tools)


@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
    """Handle tool calls"""
    try:
        async with ServiceDeskPlusClient() as client:
            result = None

            # ==================== TICKET MANAGEMENT ====================

            if name == "list_tickets":
                limit = int(arguments.get("limit", 50))
                status = arguments.get("status")
                priority = arguments.get("priority")
                requester = arguments.get("requester")
                result = await client.get_tickets(
                    limit=limit,
                    status=status,
                    priority=priority,
                    requester=requester,
                )

            elif name == "get_ticket":
                ticket_id = arguments["ticket_id"]
                result = await client.get_ticket(ticket_id)

            elif name == "search_tickets":
                query = arguments["query"]
                limit = int(arguments.get("limit", 50))
                result = await client.search_tickets(query, limit=limit)

            elif name == "get_ticket_comments":
                ticket_id = arguments["ticket_id"]
                result = await client.get_ticket_comments(ticket_id)

            elif name == "get_ticket_conversations":
                ticket_id = arguments["ticket_id"]
                result = await client.get_ticket_conversations(ticket_id)

            elif name == "get_request_tasks":
                request_id = arguments["request_id"]
                result = await client.get_request_tasks(request_id)

            elif name == "get_request_worklog":
                request_id = arguments["request_id"]
                limit = int(arguments.get("limit", 50))
                result = await client.get_request_worklog(request_id, limit)

            elif name == "get_request_attachments":
                request_id = arguments["request_id"]
                result = await client.get_request_attachments(request_id)

            elif name == "get_request_notifications":
                request_id = arguments["request_id"]
                result = await client.get_request_notifications(request_id)

            # ==================== USER MANAGEMENT ====================

            elif name == "list_users":
                limit = int(arguments.get("limit", 50))
                result = await client.get_users(limit=limit)

            elif name == "get_user":
                user_id = arguments["user_id"]
                result = await client.get_user(user_id)

            else:
                return CallToolResult(
                    content=[TextContent(type="text", text=json.dumps({"error": f"Unknown tool: {name}"}))]
                )

            return CallToolResult(
                content=[TextContent(type="text", text=json.dumps(result, ensure_ascii=False, default=str))]
            )

    except Exception as e:
        return CallToolResult(
            content=[TextContent(type="text", text=json.dumps({"error": str(e)}))]
        )


async def main():
    """Main function to run the MCP server"""
    import sys

    config_validation = Config.validate_config()
    if not config_validation["valid"]:
        print("Configuration errors:", file=sys.stderr)
        for issue in config_validation["issues"]:
            print(f"  - {issue}", file=sys.stderr)
        return

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="servicedesk-plus",
                server_version="2.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
