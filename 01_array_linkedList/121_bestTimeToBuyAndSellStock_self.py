#풀리는데 이것도 답이 되는건가?

prices = [7,6,4,3,1]

#포인터
left = 0
right = len(prices) - 1
left_min, right_max = prices[left], prices[right]

#만나기 전까지
while left < right :
    left_min = min(left_min, prices[left])
    right_max = max(right_max, prices[right])

    left += 1
    right -= 1

if right_max - left_min < 0 :
    print(0)

# print(right_max)
# print(left_min)
print(right_max - left_min)