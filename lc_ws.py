import time

from locust import User, task, events, between, TaskSet
from locust.env import Environment
from locust.web import WebUI
from flask import request

import websocket


env = Environment()

class MyTaskSet(TaskSet):
    @task
    def func1(self):
        while True:
            time.sleep(2)
            start_time = time.time()
            self.user.ws.send('abc')
            res = self.user.ws.recv()
            print(res)
            end_time = time.time()
            recv_time = int((end_time - start_time) * 1000)
            print(recv_time)
            events.request_success.fire(request_type="ws", name="请求", response_time=recv_time, response_length=0)

    @task
    def func2(self):
        while True:
            time.sleep(2)
            start_time = time.time()
            self.user.ws.send('ggg')
            res = self.user.ws.recv()
            print(res)
            end_time = time.time()
            recv_time = int((end_time - start_time) * 1000)
            print(recv_time)
            #
            events.request_success.fire(request_type="ws", name="请求", response_time=recv_time, response_length=0)


class MyUser(User):
    wait_time = between(0, 0)
    tasks = [MyTaskSet]

    def on_start(self):
        url = 'ws://192.168.1.8:8765'
        start_time = time.time()
        self.ws = websocket.create_connection(url, timeout=30)
        create_connection = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="ws", name="创建连接", response_time=create_connection, response_length=0)

    def on_stop(self):
        self.ws.close(reason='used')


web_ui = WebUI(env,host='localhost',port=8089)

@web_ui.app.route("/my_custom_route")
def my_custom_route():
    return "your IP is: %s" % request.remote_addr