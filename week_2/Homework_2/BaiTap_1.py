import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 

def SelectionSort(A): 
    for i in range(len(A)):
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i] 

elements = list() 
times = list() 
for i in range(1, 10): 

    a = randint(0, 1000 * i, 1000 * i) 
    start = time.clock() 
    SelectionSort(a) 
    end = time.clock() 

    print("Sắp xếp" , len(a)," phần tử trong ", end-start) 
    elements.append(len(a)) 
    times.append(end-start) 

plt.xlabel('List Length') 
plt.ylabel('Time Complexity') 
plt.plot(elements, times, label ='Heap Sort') 
plt.grid() 
plt.show()