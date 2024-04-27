from collections import deque

def is_palindrome(str):
    d = deque(str)
    while d.pop().lower() == d.popleft().lower():
        if not d or len(d) == 1:
            return True
    return False
        