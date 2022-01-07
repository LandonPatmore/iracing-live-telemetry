import threading
from queue import Queue
import websocket


class WebSocketSender(threading.Thread):
    def __init__(self, ws: websocket, work_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.ws = ws
        self.work_queue = work_queue

    def run(self):
        while True:
            item = self.work_queue.get(block=True)
            print("Sending %s" % item)
            self.work_queue.task_done()
