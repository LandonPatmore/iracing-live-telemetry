from asyncio import Queue
import aiohttp
import jsons

from telemetry.models.PackagedMessage import PackagedMessage


class NetworkSender:
    def __init__(self, url: str, pushable_queue: Queue):
        self.pushable_queue = pushable_queue
        self.url = url
        self.type = 0

    async def handler(self, session):
        while True:
            data = await self.pushable_queue.get()
            packaged_message = PackagedMessage(message_type=self.type, data=data)
            async with session.post(url=self.url, data=jsons.dumps(packaged_message)) as resp:
                response = await resp.text()
                print("Received response from rest api: %s" % response)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.handler(session)
