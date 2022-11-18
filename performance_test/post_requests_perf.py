from locust import HttpUser, task


class MyUserPerformanceTest(HttpUser):

    @task
    def post_url(self):
        url = '/long_url?url=https://google.com'
        response = self.client.post(url)
        _id = response.json()['response']
    