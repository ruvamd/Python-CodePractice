def is_palindrome(string):
    string = string.lower()
    left = 0
    right = len(string) - 1

    while left < right:
        if not string[left].isalnum():
            left += 1
            continue
        if not string[right].isalnum():
            right -= 1
            continue
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome('enterprise'))
print(is_palindrome('racecar'))
print(is_palindrome('never odd or even'))
print(is_palindrome('not a palindrome'))