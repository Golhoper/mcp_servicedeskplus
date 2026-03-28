# ServiceDesk Plus MCP Server

MCP-сервер для работы с ServiceDesk Plus on-premise через API v3.

## Установка и настройка

### 1. Зависимости

```bash
uv sync
```

### 2. Переменные окружения

Создай `.env` из `env.example`:

```bash
cp env.example .env
```

Заполни `.env`:

```env
SDP_BASE_URL=https://your-servicedesk-plus-instance.com
SDP_API_KEY=your_technician_api_key
```

`SDP_API_KEY` — ключ технического специалиста из SDP (Admin → Technicians → API Key).

### 3. Подключение к Claude Desktop

В `~/Library/Application\ Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "servicedesk-plus": {
      "command": "python",
      "args": ["/path/to/servicedeskplus_mcp/main.py"],
      "env": {
        "SDP_BASE_URL": "https://your-instance.com",
        "SDP_API_KEY": "your_api_key"
      }
    }
  }
}
```

## Инструменты

### Тикеты

#### `list_tickets`
Список тикетов с фильтрами.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `limit` | number | — | Кол-во результатов (по умолчанию: 50, макс: 1000) |
| `status` | string | — | Фильтр по статусу: `open`, `pending`, `resolved`, `closed`, `cancelled`, `on_hold` |
| `priority` | string | — | Фильтр по приоритету: `low`, `medium`, `high`, `critical` |
| `requester` | string | — | Email или ID заявителя |

---

#### `get_ticket`
Детальная информация о тикете.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `ticket_id` | string | + | ID тикета |

---

#### `search_tickets`
Поиск тикетов по ключевому слову.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `query` | string | + | Поисковый запрос |
| `limit` | number | — | Кол-во результатов (по умолчанию: 50, макс: 1000) |

---

#### `get_ticket_comments`
Комментарии к тикету.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `ticket_id` | string | + | ID тикета |

---

#### `get_ticket_conversations`
Переписка (email-ответы) по тикету.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `ticket_id` | string | + | ID тикета |

---

#### `get_request_tasks`
Подзадачи тикета.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `request_id` | string | + | ID тикета |

---

#### `get_request_worklog`
Журнал работ по тикету.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `request_id` | string | + | ID тикета |
| `limit` | number | — | Кол-во записей (по умолчанию: 50, макс: 1000) |

---

#### `get_request_attachments`
Вложения тикета.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `request_id` | string | + | ID тикета |

---

#### `get_request_notifications`
Уведомления, отправленные по тикету.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `request_id` | string | + | ID тикета |

---

### Пользователи

#### `list_users`
Список пользователей.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `limit` | number | — | Кол-во результатов (по умолчанию: 50, макс: 1000) |

---

#### `get_user`
Информация о пользователе.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|---------|
| `user_id` | string | + | ID пользователя |

## Устранение неполадок

**Authentication failed** — проверь `SDP_API_KEY` в `.env`. Ключ берётся из SDP: Admin → Technicians → выбери техника → Generate API Key.

**Connection Error** — проверь `SDP_BASE_URL`, убедись что инстанс доступен.

**Тест подключения:**
```bash
python test_connection.py
```
