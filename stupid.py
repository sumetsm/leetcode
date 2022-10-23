s = list(input().split(' '))
# print(s)
print(len(s)-1)
for i in range(len(s)):
    # print(i)
    if i <= len(s)-1:
        print(s.pop(-1),end='//')
        print(i)
        print(len(s))

    else :
        print(s.pop(),end='')
        # print(i)