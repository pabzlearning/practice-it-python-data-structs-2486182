from collections import deque

def check_palidrome(word):
    is_palindrome = False
    d = deque(word)

    while len(d) > 1:
        print(d)
        if d.pop() != d.popleft():
            return is_palindrome

    is_palindrome = True
    return is_palindrome

def main():
    w = "testing"
    # w = "tacocat"
    print(check_palidrome(w))
    return

if __name__ == "__main__":
    main()