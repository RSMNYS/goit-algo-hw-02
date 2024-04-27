from queue import Queue
import datetime

class Request:
    def __init__(self, text):
        self.text = text
        self.date = datetime.datetime.now()

class ServiceCenter:
    def __init__(self):
        self.requests = Queue()

    def add_request(self, request: Request):
        self.requests.put(request)

    def process_request(self):
        if not self.requests.empty():
            request = self.requests.get()
            print(f'Request is processed: {request.text}, {request.date}')
        else:
            print('Queue is empty')