import aiohttp
import asyncio

async def fetch_famous_cricketers():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.cricapi.com/v1/players?apikey=d0fb14c1-77a7-41c4-a13b-9c3394c9ba79&offset=0") as response:
                data = await response.json()
                print(data)
    except Exception as e:
        print("invalid")

asyncio.run(fetch_famous_cricketers())