from numpy.random import randint
import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(2500)


def find_min(arr, n):
    if n == 1:
        return arr[0]
    return min(arr[n - 1], find_min(arr, n - 1))


def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))


number = list()
times_min = list()
times_max = list()

for i in range(1, 11):
    t = 0
    for j in range(1, 31):
        a = randint(0, 200 * i, 200 * i)
        start = time.process_time()
        find_min(a, len(a))
        end = time.process_time()
        t += end - start

    number.append(len(a))
    times_min.append(t / 30)

for i in range(1, 11):
    t = 0
    for j in range(1, 31):
        a = randint(0, 200 * i, 200 * i)
        start = time.process_time()
        find_max(a, len(a))
        end = time.process_time()
        t += end - start
    times_max.append(t / 30)

fig, (plot_min, plot_max) = plt.subplots(1, 2, tight_layout = True)
plot_min.plot(number, times_min, 'ro')
plot_min.set_xlabel('Số phần tử của mảng')
plot_min.set_ylabel('Thời gian chạy')
plot_min.set_title('Tìm min')
plot_min.grid()

plot_max.plot(number, times_max, 'bo')
plot_max.set_xlabel('Số phần tử của mảng')
plot_max.set_ylabel('Thời gian chạy')
plot_max.set_title('Tìm max')
plot_max.grid()

plt.show()