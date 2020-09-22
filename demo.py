from locust import HttpUser, task, between, User, constant, tag, TaskSet, SequentialTaskSet


# class QuickstartUser(HttpUser):
#     wait_time = between(0, 0)
#
#     @task
#     def index_page(self):
#         self.client.get('/hello')
#         self.client.get('/world')
#
#     @task(3)
#     def view_item(self):
#         for item_id in range(10):
#             self.client.get(f'/item?id={item_id}', name="/item")
#
#     def on_start(self):
#         self.client.post('/login', json={'username': 'foo', 'password': 'bar'})
from locust.contrib.fasthttp import FastHttpUser


class ForumSection(TaskSet):

    @task
    def func1(self):
        print('func1')

    @task
    def func2(self):
        print('func2')

    @task
    def func3(self):
        print('func3')

    @task
    def stop(self):
        self.interrupt()


class SequenceOfTasks(SequentialTaskSet):
    @task
    def first_task(self):
        print('first_task')

    @task
    def second_task(self):
        print('second_task')

    @task
    def third_task(self):
        print('third_task')


class MyUser(User):

    def fun4(self):
        print('fun4')

    tasks = {SequenceOfTasks: 2}
    wait_time = constant(1)


class MyTaskSet(TaskSet):

    @task
    def index(self):
        with self.client.get('/',catch_response=True) as res:
            if res.status_code != 200:
                res.failure('status_cod != 200')

    @task
    def about(self):
        res = self.client.get('/about')
        print(res.status_code)
        print(res.text)

    @task
    def item(self):
        for i in range(10):
            self.client.get(f"/item?item_id={i}", name=f"/item?item_id={i}")


class MyHttpUser(FastHttpUser):
    wait_time = between(5, 15)
    tasks = [MyTaskSet]
