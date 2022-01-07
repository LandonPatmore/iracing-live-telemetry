import threading
from queue import Queue
import jsons
import requests


class NetworkSender(threading.Thread):
    def __init__(self, url: str, pushable_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.pushable_queue = pushable_queue
        self.url = url

    def run(self):
        while True:
            item = self.pushable_queue.get(block=True)
            requests.post(self.url, data=jsons.dumps(item))
            self.pushable_queue.task_done()
