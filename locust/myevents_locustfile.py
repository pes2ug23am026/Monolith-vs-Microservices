from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_my_events(self):
        self.client.get("/my-events?user=PES2UG23AM026")
