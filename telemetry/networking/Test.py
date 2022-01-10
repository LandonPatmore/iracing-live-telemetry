import asyncio

import websockets

async def consumer_handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)


async def consumer(message):
    print("The message is: %s" % message)


async def producer_handler(websocket):
    while True:
        message = await producer()
        await websocket.send(message)


async def producer() -> str:
    await asyncio.sleep(0)
    return "This is a test message"


async def handler(websocket):
    consumer_task = asyncio.create_task(consumer_handler(websocket))
    producer_task = asyncio.create_task(producer_handler(websocket))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()


async def hello():
    uri = "ws://localhost:7000/telemetry/1234"
    async with websockets.connect(uri) as websocket:
        await handler(websocket)


if __name__ == "__main__":
    # asyncio.get_event_loop().create_task(hello())
    asyncio.run(hello())
    # asyncio.get_event_loop().run_forever()
