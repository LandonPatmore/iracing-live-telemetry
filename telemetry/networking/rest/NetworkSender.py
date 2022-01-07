import threading
from queue import Queue


class NetworkSender(threading.Thread):
    def __init__(self, pushable_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.pushable_queue = pushable_queue

    def run(self):
        while True:
            item = self.pushable_queue.get(block=True)
            print("Pushing %s" % item)
            self.pushable_queue.task_done()
