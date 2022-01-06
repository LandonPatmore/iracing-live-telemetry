import _thread
from queue import Queue
import threading

from classes.MessageTypes import GENERAL_INFO, TELEMETRY
from telemetry.TelemetryLogger import TelemetryLogger
from telemetry.WebSocketHandler import WebSocketHandler

work_queue = Queue()
websocket_handler = WebSocketHandler(websocket_url="ws://localhost:7000/telemetry/1234", work_queue=work_queue)
telemetry_logger = TelemetryLogger(websocket_handler)

if __name__ == "__main__":
    # TODO: Daemon threads
    websocket_handler.start()
    while True:
        item = work_queue.get(block=True)
        if item == GENERAL_INFO:
            print("general info requested")
        elif item == TELEMETRY:
            print("start sending iracing data")
            telemetry_logger.start()
        work_queue.task_done()
