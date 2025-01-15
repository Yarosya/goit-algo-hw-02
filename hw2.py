from collections import deque
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("Козак з казок"))
print(is_palindrome("шалаш"))