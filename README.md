# ServiceDesk Plus MCP Server

MCP-сервер для работы с ServiceDesk Plus on-premise через API v3.

## Инструменты

**Тикеты:** `list_tickets`, `get_ticket`, `search_tickets`, `get_ticket_comments`, `get_ticket_conversations`, `get_request_tasks`, `get_request_worklog`, `get_request_attachments`, `get_request_notifications`

**Пользователи:** `list_users`, `get_user`

## Установка

```bash
uv sync
cp env.example .env
# заполни .env
```

## Подключение к Claude Desktop

```json
{
  "mcpServers": {
    "servicedesk-plus": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/servicedeskplus_mcp", "python", "main.py"],
      "env": {
        "SDP_BASE_URL": "https://your-instance.com",
        "SDP_API_KEY": "your_technician_api_key"
      }
    }
  }
}
```

Подробнее — [USAGE.md](USAGE.md).
