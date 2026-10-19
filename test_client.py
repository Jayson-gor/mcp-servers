import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8002/mcp") as client:
        tools = await client.list_tools()
        print([t.name for t in tools])
        print(await client.call_tool(tools[0].name, {"a": 2, "b": 3}))

asyncio.run(main())