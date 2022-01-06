import threading
import jsons
import websocket
from queue import Queue


class WebSocketHandler(threading.Thread):
    def __init__(self, websocket_url: str, work_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.ws: websocket = self.__create_websocket(websocket_url)
        self.work_queue = work_queue

    @staticmethod
    def __create_websocket(url: str) -> websocket:
        return websocket.create_connection(url)

    def send_data(self, data):
        self.ws.send(data)

    def run(self):
        while True:
            message = jsons.loads(self.ws.recv())

            print("message received: %s" % message)

            if "type" in message:
                self.work_queue.put(message["type"])
            else:
                print("message not formatted correctly")
