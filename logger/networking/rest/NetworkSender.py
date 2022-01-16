from asyncio import Queue
import aiohttp
import jsons


class NetworkSender:
    def __init__(self, url: str, pushable_queue: Queue):
        self.pushable_queue = pushable_queue
        self.url = url

    async def handler(self, session):
        while True:
            data = await self.pushable_queue.get()
            async with session.post(url=self.url, data=data) as resp:
                response = await resp.text()
                print("Received response from rest api: %s" % response)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.handler(session)
