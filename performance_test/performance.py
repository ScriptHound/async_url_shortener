from locust import HttpUser, task


class MyUserPerformanceTest(HttpUser):

    def on_start(self):
        self.ids = []

    @task(50)
    def post_url(self):
        url = '/long_url?url=https://google.com'
        for _ in range(100):
            response = self.client.post(url)
            _id = response.json()['response']
            self.ids.append(_id)
    