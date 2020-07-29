import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(2500)
times = list()
number = list()


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Kiểm tra tính đúng

for i in range(0,21,5):
    f = Fibonacci(i)
    print(f)

# Kiểm tra độ phức tạp
for i in range(0, 36, 5):
    t = 0
    for j in range(1, 31):
        start = time.process_time()
        Fibonacci(i)
        end = time.process_time()
        t += end - start

    number.append(i)
    times.append(t / 30)
plt.ylabel('Thời gian chạy')
plt.xlabel('Giá trị của n')
plt.grid()
plt.plot(number, times, 'ro')
for a, b in zip(number, times):
    plt.text(a, b, '{0:.4f}'.format(b))
plt.show()
