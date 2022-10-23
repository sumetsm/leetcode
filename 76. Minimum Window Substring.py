
def minWindow(s, t):
    lenght_s = len(s)
    lenght_t = len(t)
    res = ''
    if s == t :
        return res.join(s)
    # win_min = 0
    for win_min in range(lenght_s+1) :
        for i in range(lenght_s - win_min + 1):
            res_stk = []
            check_stk = list(t)
            for j in range(i,i+win_min):
                print(s[j],j)
                res_stk.append(s[j])
                if s[j] in check_stk:
                    # indexc = check_stk.index(s[j])
                    check_stk.remove(s[j])
                if check_stk == []:
                    print('found !!')
                    res = ''.join(res_stk)
                    return res
            print('---------')
    return res

print(minWindow("izmlkeypagilhagznujolmmvxzdelmcvlogyugpxpyiwyrwllhaywmutlzzylcvzsbxpjmoykwx",
"jntwbc"))