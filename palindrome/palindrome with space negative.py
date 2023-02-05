def is_palindrome(string):
    string = string.lower()
    string = "".join(c for c in string if c.isalnum())
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome('enterprise'))
print(is_palindrome('racecar'))
print(is_palindrome('never odd or even'))
print(is_palindrome('not a palindrome'))