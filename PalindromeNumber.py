import re


def isPalindrome(x):
    print(x)
    ans = True
    if x < 0 :
        return False
    ls = []
    while x > 0:
        y = int(x % 10)
        x =x-y
        x = x / 10
        ls.insert(0,y)
    for i in range(int(len(ls)/2)):
        if ls[i] != ls[-(i+1)]:
            return False
    return ans


print(isPalindrome(123421))
print("hello")
