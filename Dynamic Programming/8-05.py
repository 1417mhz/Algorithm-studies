# Dynamic Programming
# p.217

# 정수 x가 1이 될 때 까지 다음의 연산을 실행한다.
# 연산을 사용하는 최소 횟수를 구하시오. 

x = int(input())

# 계산된 결과를 저장하기 위한 DP 테이블
d = [0] * 30001

# 다이나믹 프로그래밍 진행(Bottom-Up)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 2)
    # 현재의 수가 5로 나누어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        
print(d[x])