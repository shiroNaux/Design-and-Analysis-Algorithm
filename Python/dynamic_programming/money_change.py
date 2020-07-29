import math


def count(arr, right):
    dynamic = [math.inf] * (right + 1)

    for j in arr:
        dynamic[j] = 1

    for j in range(1, right + 1):
        re = list()
        if dynamic[j] == math.inf:
            for k in range(1, j // 2 + 1):
                re.append(dynamic[k] + dynamic[j - k])

        if len(re) != 0:
            dynamic[j] = min(re)

    return dynamic


def backward(value):
    if number_money[value] == 1:
        index = money.index(value)
        result[index] += 1
    else:
        for i in range(1, value // 2 + 1):
            if (number_money[i] + number_money[value - i]) == number_money[value]:
                backward(i)
                backward(value - i)
                break


money = [10, 6, 1]
number_money = count(money, 55)
result = [0] * len(money)
backward(55)

print("Số các tờ tiền", money,"cần dùng là", result)
