from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    # интервал между запросами (имитируем «пользователей»)
    wait_time = between(0.1, 0.3)

    @task
    def index(self):
        self.client.get("/")  # ваш minikube URL + "/"
