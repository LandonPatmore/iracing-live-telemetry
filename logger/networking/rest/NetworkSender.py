from asyncio import Queue
import aiohttp
import jsons

from logger.models.MessageTypes import PUSHABLE_AGGREGATOR_MESSAGE
from logger.models.PackagedMessage import PackagedMessage


class NetworkSender:
    def __init__(self, url: str, pushable_queue: Queue):
        self.pushable_queue = pushable_queue
        self.url = url

    async def handler(self, session):
        while True:
            data = await self.pushable_queue.get()
            packaged_message = PackagedMessage(message_type=PUSHABLE_AGGREGATOR_MESSAGE, data=data)
            async with session.post(url=self.url, data=jsons.dumps(packaged_message)) as resp:
                response = await resp.text()
                print("Received response from rest api: %s" % response)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            await self.handler(session)