#sort()

nums = [1,4,3,2]

result = 0

nums.sort()
for i in range(len(nums)//2) :
    result += min(nums[i*2], nums[i*2+1])

print(result)