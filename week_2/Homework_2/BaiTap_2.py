import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 

elements = list()
times = list()

def find(x):
    for i in a:
        if a[i] == x:
            return i
    return 0

for i in range(1, 10): 
    a = randint(0, 100000 * i, 100000 * i)
    x = 100000*i + 1
    start = time.clock() 
    xx = find(x)
    end = time.clock()
    
    print("Tìm giá trị", x ,"trong mảng ", len(a),"phần tử từ 0 đến", len(a),"tại vị trí", xx, "trong thời gian ", end-start)
    elements.append(len(a))
    times.append(end-start)

plt.xlabel('List Length') 
plt.ylabel('Time Complexity') 
plt.plot(elements, times, label ='Heap Sort') 
plt.grid() 
plt.legend()
plt.show()