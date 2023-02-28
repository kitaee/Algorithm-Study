#1149번 RGB거리

n = int(input())
p = []

#input 값 이차원 배열로 생성
for i in range(n):
    p.append(list(map(int, input().split())))

#두번째 집부터 앞 집과 비교하여 누적해야 하므로 시작은 인덱스 1부터
for i in range(1, n):
    p[i][0] = p[i][0] + min(p[i-1][1],p[i-1][2])
    p[i][1] = p[i][1] + min(p[i-1][0],p[i-1][2])
    p[i][2] = p[i][2] + min(p[i-1][0],p[i-1][1])

print(min(p[n-1][0],p[n-1][1],p[n-1][2]))
