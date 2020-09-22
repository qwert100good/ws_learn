import asyncio
import time

import websockets
from websockets import ConnectionClosed


# WS server example


async def handler(websocket, path):
    # 获取ip
    remote_ip = websocket.remote_address[0]
    # print(remote_ip)
    try:
        async for message in websocket:
            await asyncio.sleep(2)
            await websocket.send(f'you commit {message}')
    except ConnectionClosed:
        print(f'{remote_ip} 链接中断了！！')


start_server = websockets.serve(handler, '192.168.1.8', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
