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

#Kiểm tra tính đúng

for i in range(0, 51,5):
    for j in range(1,6):
        result = reward(i,j,0)
        print("Số cách chia ",i," phần thưởng cho ", j," học sinh:" , result)

# Kiểm tra độ phức tạp
elements = list()
times = list()

for i in range(100, 1001, 50):
    t = 0
    for j in range(1,31):
        start = time.process_time()
        reward(i, 5,0)
        end = time.process_time()
        t += end - start

    times.append(t/30)
    elements.append(i)

plt.plot(elements, times)
plt.grid()
plt.show()
