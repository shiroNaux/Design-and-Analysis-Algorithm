import time
import matplotlib.pyplot as plt


def reward(m, n, x):
    if (m == 0 or n == 1 or m == 1):
        return 1;
    else:
        y = 0
        a = m // n
        for i in range(x, a + 1, 1):
            y += reward(m - i, n - 1, i)

        return y


elements = list()
times = list()

for i in range(100, 1001, 50):
    start = time.process_time()
    reward(i, 5)
    end = time.process_time()
    times.append(end - start)
    elements.append(i)

plt.plot(elements, times)
plt.grid()
plt.show()