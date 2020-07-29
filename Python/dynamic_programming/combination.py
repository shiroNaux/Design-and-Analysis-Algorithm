def combination(n, k):
    dynamic = [[0 for x in range(k + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, min(i + 1, k + 1)):
            if j == 0 or j == 1:
                dynamic[i][j] = i * j
            else:
                dynamic[i][j] = dynamic[i - 1][j - 1] + dynamic[i - 1][j]
    return dynamic[n][k]


x = 10
y = 5
result = combination(x, y)
print("Tổ hợp chập ", y," của ", x,"là: ", result)

