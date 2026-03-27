#!/usr/bin/env python3
"""Test connection to ServiceDesk Plus"""

import asyncio
from sdp_client import ServiceDeskPlusClient
from config import Config


async def main():
    print(f"Connecting to: {Config.SDP_BASE_URL}")

    config = Config.validate_config()
    if not config["valid"]:
        for issue in config["issues"]:
            print(f"  Config error: {issue}")
        return

    async with ServiceDeskPlusClient() as client:
        if not await client.authenticate():
            print("Authentication failed")
            return
        print("Authentication OK")

        tickets = await client.get_tickets(limit=5)
        requests = tickets.get("requests", [])
        print(f"Tickets: {len(requests)} fetched")

        users = await client.get_users(limit=5)
        print(f"Users: {len(users.get('requester', []))} fetched")


if __name__ == "__main__":
    asyncio.run(main())
