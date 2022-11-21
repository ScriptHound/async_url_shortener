import csv
from random import choice
from locust import HttpUser, task


class MyUserPerformanceTest(HttpUser):

    def on_start(self):
        self.test_data = []
        with open('redis_data_dump.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.test_data.append(row['key'])

    @task
    def get_url(self):
        for _ in range(250):
            random_key = choice(self.test_data)
            url = f'/resolved_url/{random_key}'
            response = self.client.get(url)