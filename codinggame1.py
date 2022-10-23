s = "Hello <World Na Ja> pleum"
stk = []
check = False
for i in s:
    if i =='>':
        check = False   
    if check == True:
        stk.append(i)
    if i =='<':
        check = True
print(str(stk))  
        
# for e in ans :
    
#     print(e)