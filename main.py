from double_queue import is_palindrome
from requests_queue import Request, ServiceCenter


def main():
    while True:
        user_input = input('Please add your request to process. If you want to exit, type "exit": ')
        if user_input == 'exit':
            break
        if (len(user_input) == 0):
            print('Wrong input. Try again.')            
        else:
            if is_palindrome(user_input):
                print('Just a note, your input is a palindrome')
            service_center = ServiceCenter()
            request = Request(user_input)
            service_center.add_request(request)
            service_center.process_request()

if __name__ == '__main__':
    main()