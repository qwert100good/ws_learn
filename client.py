import websockets
import asyncio


async def hello(i):
    uri = "ws://192.168.1.8:8765"

    async with websockets.connect(uri) as websocket:
        for count in range(10):
            await websocket.send(f'次数{count} test {i}')


async def main():
    tasks = []
    for i in range(10):
        task = asyncio.gather(hello(i, ))
        tasks.append(task)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
