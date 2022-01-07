import threading

import jsons
import websocket
from queue import Queue


class WebSocketReceiver(threading.Thread):
    def __init__(self, ws: websocket, work_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.ws = ws
        self.work_queue = work_queue

    def run(self):
        while True:
            message = jsons.loads(self.ws.recv())

            print("message received: %s" % message)

            if "send" in message:
                self.work_queue.put(message["send"])
            else:
                print("message not formatted correctly")
