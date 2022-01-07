import threading
from queue import Queue


class NetworkSender(threading.Thread):
    def __init__(self, pushing_queue: Queue):
        threading.Thread.__init__(self, daemon=True)
        self.pushing_queue = pushing_queue

    def run(self):
        while True:
            item = self.pushing_queue.get(block=True)
            print("Pushing %s" % item)
            self.pushing_queue.task_done()
