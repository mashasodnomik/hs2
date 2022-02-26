import requests


data = {"full_name": "Тест нейм 1",
        "phone": "213213124124",
        "email": "asdasdas@asfas.asdfa",
        "login": "asdasd",
        "password": "213"}
response =requests.post("http://127.0.0.1:5000/employee", json=data)
print(response.json())