def sub_array(array):
    dynamic = [1] * len(array)
    i = 1
    maximum = array[0]
    sub = 1
    while i < len(array):
        if array[i] > maximum:
            dynamic[i] = sub + 1
            sub = dynamic[i]
            maximum = array[i]
        else:
            result = list()
            for j in range(0, i):
                if array[i] > array[j]:
                    result.append(dynamic[j])
                dynamic[i] = max(result, default=0) + 1

        i += 1
    return dynamic


def rollback(matrix):
    re = list()
    maximum = max(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[i] == maximum:
            re.append(arr[i])
            maximum -= 1
    return re


arr = [2,5,4,6,3,8,9,7]
longest = sub_array(arr)
numbers = rollback(longest)
print("Dãy con tăng dài nhất là: ", numbers[::-1])

