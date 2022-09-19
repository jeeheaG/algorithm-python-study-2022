#그래프 시각화 후 풀이 - 저점을 기준으로 잡고 고점 체크하며 교체
import sys

prices = [7,1,5,3,6,4]

profit = 0
minPrice = sys.maxsize # 시스템 상 가장 큰 값으로 설정

for p in prices :
    #저점(최소값) 갱신
    minPrice = min(p, minPrice)

    #profit 계산하여 최대값으로 갱신
    profit = max(profit, p - minPrice)

print(profit)
