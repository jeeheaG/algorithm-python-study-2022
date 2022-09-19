#sum even nums

nums = [1,4,3,2]

result = 0

for i, n in enumerate(nums) :
    if i%2 == 0 :
        result += n

print(result)