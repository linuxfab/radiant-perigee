H, W, N = map(int, input().split())  # 讀取 H, W, N
r = [0] * N
c = [0] * N
t = [0] * N
x = [0] * N

for i in range(N):
    r[i], c[i], t[i], x[i] = map(int, input().split())

for row in range(H):
    for col in range(W):
        color = 0
        for number in range(N):
            if (abs(row-r[number]) + abs(row-r[number]))  <= t[number]
                color +=x[number]
        print(color, end=" ")
    print("")
