import heapq

N, K = (int(x) for x in input().split())
machine_list = []
for i in range(N):
    heapq.heappush(machine_list, list(map(lambda x: int(x), input().split())))

sum = 0
for _ in range(K):
    macheni = heapq.heappop(machine_list)
    sum += macheni[0]
    macheni[0] += macheni[1]
    heapq.heappush(machine_list, macheni)

print(sum)
