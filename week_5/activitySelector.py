def activitySelector(A):
    S = list()
    A.sort(key = lambda x: x[1])
    j = 0
    S.append(A[0])
    for i in range(2, len(A)):
        if A[i][0] >= A[j][1]:
            S.append(A[i])
            j = i

    return S


# dữ liệu lấy trong slide bài giảng
activity = [[1, 3], [1, 8], [2, 5], [4, 7], [5, 9], [8, 10], [9, 11], [11, 14], [13, 16]]
print("Các hoạt động cần chọn là: ", activity)
result = activitySelector(activity)
print("Các hoạt động được chọn là: ", result)
