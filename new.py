nums =[-1,0,1,2,-1,-4,3,1,3,-2,-3]
temp = []
res = []
for i in range (len(nums)-3):
    for j in range(i+1,len(nums)-2):
        for k in range(j+1,len(nums)-1):
            if nums[i]+nums[j]+nums[k] == 0:
                temp.append(nums[i])
                temp.append(nums[j])
                temp.append(nums[k])
                temp.sort()
                if temp not in res :
                    res.insert(0,temp)
                temp =[]
print(res)