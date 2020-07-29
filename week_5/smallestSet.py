import random
import numpy


def smallest_t(element):
    element.sort()

    smallest_set = list()
    left = float('-inf')
    for p in element:
        if left <= p:
            interval = (p, p + 1)
            smallest_set.append(interval)
            left = p + 1
    return smallest_set


numbers = list()
for i in range(1, 31):
    x = round(random.uniform(1, 10), 2)
    numbers.append(x)

points = numpy.array(numbers)


result = smallest_t(numbers)
print("Các số cần phân  khoảng là: ", points)
print("Số lượng các khoảng nhỏ nhất là: ", len(result))
print('Các khoảng là:\n', result)
