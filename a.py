import sys

def solve():
    # 使用 sys.stdin.readline 提高讀取速度
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    H, W, N = map(int, input_data[:3])
    idx = 3
    
    # 座標旋轉: u = r + c, v = r - c
    # u 範圍: 0 能量到 H + W - 2
    # v 範圍: -(W - 1) 到 H - 1 -> 偏移 W - 1 變為 0 到 H + W - 2
    
    max_dim = H + W
    # 建立 2D 差分陣列
    # 尺寸設大一點避免索引越界
    diff = [[0] * (max_dim + 1) for _ in range(max_dim + 1)]
    
    v_offset = W - 1
    
    for _ in range(N):
        r_i = int(input_data[idx])
        c_i = int(input_data[idx+1])
        t_i = int(input_data[idx+2])
        x_i = int(input_data[idx+3])
        idx += 4
        
        u_i, v_i = r_i + c_i, r_i - c_i
        
        # 矩形邊界: [u1, u2] x [v1, v2]
        u1 = max(0, u_i - t_i)
        u2 = min(H + W - 2, u_i + t_i)
        v1 = max(0, v_i - t_i + v_offset)
        v2 = min(H + W - 2, v_i + t_i + v_offset)
        
        if u1 <= u2 and v1 <= v2:
            # 2D 差分更新
            diff[u1][v1] += x_i
            diff[u1][v2 + 1] -= x_i
            diff[u2 + 1][v1] -= x_i
            diff[u2 + 1][v2 + 1] += x_i
            
    # 計算二維前綴和
    for i in range(max_dim + 1):
        for j in range(1, max_dim + 1):
            diff[i][j] += diff[i][j - 1]
            
    for i in range(1, max_dim + 1):
        for j in range(max_dim + 1):
            diff[i][j] += diff[i - 1][j]
            
    # 輸出結果
    results = []
    for r in range(H):
        row_res = []
        for c in range(W):
            u = r + c
            v = r - c + v_offset
            row_res.append(str(diff[u][v]))
        results.append(" ".join(row_res))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()