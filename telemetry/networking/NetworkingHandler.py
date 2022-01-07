import websocket
from queue import Queue
from telemetry.networking.rest.NetworkSender import NetworkSender
from telemetry.networking.websockets.WebSocketReceiver import WebSocketReceiver
from telemetry.networking.websockets.WebSocketSender import WebSocketSender


class NetworkingHandler:
    def __init__(self, websocket_url: str, rest_url: str, receiver_queue: Queue, streaming_queue: Queue,
                 pushable_queue: Queue):
        self.ws: websocket = self.__create_websocket(url=websocket_url)
        self.websocket_receiver = WebSocketReceiver(ws=self.ws, work_queue=receiver_queue)
        self.websocket_sender = WebSocketSender(ws=self.ws, work_queue=streaming_queue)
        self.network_sender = NetworkSender(url=rest_url, pushable_queue=pushable_queue)

    @staticmethod
    def __create_websocket(url: str) -> websocket:
        return websocket.create_connection(url)

    def start(self):
        self.websocket_receiver.start()
        self.websocket_sender.start()
        self.network_sender.start()
