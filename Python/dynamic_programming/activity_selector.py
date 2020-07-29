def selection(arr):
    arr.sort(key=lambda x: x[1])
    dynamic = [1] * len(arr)
    i = 1
    maximum = arr[0][1]
    sub = 1

    while i < len(arr):
        if arr[i][0] > maximum:
            dynamic[i] = sub + 1
            sub = dynamic[i]
            maximum = arr[i][1]
        else:
            result = list()
            for j in range(0, i):
                if arr[i][0] > arr[j][1]:
                    result.append(dynamic[j])
                dynamic[i] = max(result, default=0) + 1

        i += 1
    return dynamic


def rollback(matrix):
    result = list()
    maximum = max(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[i] == maximum:
            result.append(activity[i])
            maximum -= 1
    return result


activity = [[1, 3], [1, 8], [2, 5], [4, 7], [5, 9], [8, 10], [9, 11], [11, 14], [13, 16]]
selected = selection(activity)
r = rollback(selected)
print("Dãy các hoạt động được chọn là: ", r[::-1])
