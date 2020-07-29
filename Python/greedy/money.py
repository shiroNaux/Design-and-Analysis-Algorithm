def changeMoney(A, T):
    S = [0] * len(A)
    i = 0;
    A.sort(reverse=True)
    while (i <= len(A) and T > 0):
        S[i] = T // A[i]
        T -= S[i] * A[i]
        i += 1

    if T > 0:
        return -1
    else:
        return S


T = 55
money = [1, 10, 6]
result = changeMoney(money, T)
print("Đổi ", T, "ra các tờ tiền có mệnh giá", sorted(money))
print("Cần số tờ tiền tương ứng là: ", result)