import websocket
from queue import Queue

from telemetry.networking.websockets.WebSocketReceiver import WebSocketReceiver
from telemetry.networking.websockets.WebSocketSender import WebSocketSender


class WebSocketHandler:
    def __init__(self, websocket_url: str, receiver_queue: Queue, streaming_queue: Queue):
        self.ws: websocket = self.__create_websocket(url=websocket_url)
        self.websocket_receiver = WebSocketReceiver(ws=self.ws, work_queue=receiver_queue)
        self.websocket_sender = WebSocketSender(ws=self.ws, work_queue=streaming_queue)

    @staticmethod
    def __create_websocket(url: str) -> websocket:
        return websocket.create_connection(url)

    def start(self):
        self.websocket_receiver.start()
        self.websocket_sender.start()
