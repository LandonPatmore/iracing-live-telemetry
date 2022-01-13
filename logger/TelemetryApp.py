import asyncio
from asyncio import Queue

from logger.TelemetryLogger import TelemetryLogger
from logger.networking.NetworkingHandler import NetworkingHandler

pushable_queue = Queue()
receiver_queue = Queue()
streaming_queue = Queue()
telemetry_logger = TelemetryLogger(receiver_queue=receiver_queue, pushable_queue=pushable_queue,
                                   streaming_queue=streaming_queue)
networking_handler = NetworkingHandler(websocket_url="ws://localhost:7000/logger",
                                       rest_url="http://localhost:7000/logger",
                                       receiver_queue=receiver_queue,
                                       streaming_queue=streaming_queue, pushable_queue=pushable_queue)


async def main():
    telemetry = asyncio.create_task(telemetry_logger.run())
    networking = asyncio.create_task(networking_handler.run())
    done, pending = await asyncio.wait(
        [telemetry, networking],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().create_task(main())
    asyncio.get_event_loop().run_forever()
