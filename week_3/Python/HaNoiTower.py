import matplotlib.pyplot as plt
import time

number = list()
times = list()


def HaNoiTower(n, fromDisk, toDisk, tempDisk):
    x = 0
    if n == 0:
        return 0;
    if n == 1:
        x += 1
        return
    HaNoiTower(n - 1, fromDisk, tempDisk, toDisk)
    x += 1
    HaNoiTower(n - 1, tempDisk, toDisk, fromDisk)


if __name__ == '__main__':
    for i in range(0, 26, 5):  # Thực hiện với giá trị khác nhau của input
        t = 0
        for j in range(1, 31):  # thực hiện 30 lần với mỗi giá trị của n
            start = time.process_time()
            HaNoiTower(i, "A", "B", "C")
            end = time.process_time()
            t += end - start
        times.append(t / 30)
        number.append(i)

    plt.grid()
    plt.plot(number, times, 'ro')
    plt.ylabel('Thời gian chạy')
    plt.xlabel('Giá trị của n')
    for a, b in zip(number, times):
        plt.text(a, b, '{0:.4f}'.format(b))

    plt.show()
