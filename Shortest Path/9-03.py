# 플로이드 워셜 알고리즘 (최단 거리 알고리즘)
# p.257

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 거리를 '무한'이라고 출력
        if graph[a][b] == INF:
            print('Infinite', end=" ")
        else:
            print(graph[a][b], end=" ")
            
    print()
