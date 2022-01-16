import asyncio
from asyncio import Queue
from networking.rest.NetworkSender import NetworkSender

from networking.websockets.WebsocketHandler import WebsocketHandler


class NetworkingHandler:
    def __init__(self, websocket_url: str, rest_url: str, receiver_queue: Queue, streaming_queue: Queue,
                 pushable_queue: Queue):
        self.websocket_handler = WebsocketHandler(url=websocket_url, receiver_queue=receiver_queue,
                                                  streaming_queue=streaming_queue)
        self.network_sender = NetworkSender(url=rest_url, pushable_queue=pushable_queue)

    async def run(self):
        websocket = asyncio.create_task(self.websocket_handler.run())
        rest = asyncio.create_task(self.network_sender.run())
        done, pending = await asyncio.wait(
            [websocket, rest],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
