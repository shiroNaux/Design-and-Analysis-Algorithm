def knapsack(value, weight, capacity):
    value.insert(0, 0)
    weight.insert(0, 0)

    n = len(value) - 1

    m = [[0] * (capacity + 1) for _ in range(n + 1)]

    for w in range(capacity + 1):
        m[0][w] = 0

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i] > w:
                m[i][w] = m[i - 1][w]
            else:
                m[i][w] = max(m[i - 1][w - weight[i]] + value[i],
                              m[i - 1][w])

    return m


def backward(arr, weight):
    back = list()
    m = len(arr) - 1
    n = len(arr[0]) - 1

    while True:
        if arr[m][n] == 0:
            break
        if arr[m][n] == arr[m - 1][n]:
            m -= 1
            n -= 1
        else:
            back.append(m)
            m -= 1
            n = n - weight[m]
    return back


values = [3, 2, 2, 1]
weights = [2, 1, 2, 1]
result = knapsack(values, weights, 4)
r = backward(result, weights)
print("Các đồ vật cho và ba lô là: ", r[::-1])
print("Tổng giá trị lớn nhất là: ", max(max(result)))
