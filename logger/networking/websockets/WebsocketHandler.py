import asyncio
from asyncio import Queue
import websockets


class WebsocketHandler:
    def __init__(self, url: str, receiver_queue: Queue, streaming_queue: Queue):
        self.receiver_queue: Queue = receiver_queue
        self.streaming_queue: Queue = streaming_queue
        self.url = url

    async def consumer_handler(self, websocket):
        async for message in websocket:
            await self.receiver_queue.put(message)

    async def producer_handler(self, websocket):
        while True:
            data = await self.streaming_queue.get()
            await websocket.send(data)

    async def handler(self, websocket):
        consumer_task = asyncio.create_task(self.consumer_handler(websocket))
        producer_task = asyncio.create_task(self.producer_handler(websocket))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def run(self):
        async with websockets.connect(self.url) as websocket:
            await self.handler(websocket)
