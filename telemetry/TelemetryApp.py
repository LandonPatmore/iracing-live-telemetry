from queue import Queue
from telemetry.TelemetryLogger import TelemetryLogger
from telemetry.networking.NetworkingHandler import NetworkingHandler

pushable_queue = Queue()
receiver_queue = Queue()
streaming_queue = Queue()
networking_handler = NetworkingHandler(websocket_url="ws://localhost:7000/telemetry/1234", receiver_queue=receiver_queue,
                                       streaming_queue=streaming_queue, pushable_queue=pushable_queue)
telemetry_logger = TelemetryLogger(receiver_queue=receiver_queue, pushable_queue=pushable_queue,
                                   streaming_queue=streaming_queue)

if __name__ == "__main__":
    networking_handler.start()
    telemetry_logger.start()
    while True:
        pass
