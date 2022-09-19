# two pointer

# def trap(self, height: List[int]) -> int :

height = [0,1,0,2,1,0,1,3,2,1,2,1]

#빈 인풋값이 들어왔을 경우를 처리
if not height :
	print(0)

left = 0
right = len(height) - 1 #포인터 0부터 시작
left_max, right_max = height[left], height[right]
volume = 0

while left < right : #서로 만나기 전까지 실행
	#왼, 오 최댓값을 현재값과 비교해 갱신
	left_max = max(left_max, height[left])
	right_max = max(right_max, height[right])

	#더 작은 값이 큰 값쪽으로 한 칸 이동, 이동하면서 볼륨(빗물) 계산해 더함
	if left_max <= right_max :
		#만약 위에서 갱신이 되어서(현재값이 최대 높이 막대임) 두 값이 동일하다면 0만 더해짐
		#만약 위에서 갱신이 되지 않았다면(현재값이 최대 높이 막대보다 낮음) 양의 값인 빗물양이 더해짐
		volume += left_max - height[left]
		left += 1
	else :
		#동일
		volume += right_max - height[right]
		right -= 1

print(volume)
