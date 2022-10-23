import re


def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        for i in range(len(s)):
            stk= []
            stk.append(s[i])
            for j in range(i,len(s)):
                # print(stk)
                if j+1 == len(s):
                    result.append(stk)
                    stk = []
                    stk.append(s[i])
                    break
                if s[j+1] not in stk:
                    stk.append(s[j+1])
                elif s[j] in stk or j == len(s):
                    result.append(stk)
                    stk = []
                    stk.append(s[i])
                    break

        return len(max(result, key=len))

    # return 
s1 = 'werwrwerwer'
s = 'asdfkabdkfbasd'
result = lengthOfLongestSubstring(s)
print(result)