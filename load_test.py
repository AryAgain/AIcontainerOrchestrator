import requests
from time import sleep
import threading

def send_requests(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    url = "http://localhost:8080"
    threads = []

    for i in range(10):  # Number of threads to simulate load
        thread = threading.Thread(target=send_requests, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

