from queue import PriorityQueue

edge = PriorityQueue()
edge.put((5, [0, 3]))
edge.put((7, [0, 1]))
edge.put((8, [1, 2]))
edge.put((5, [2, 4]))
edge.put((9, [3, 1]))
edge.put((15, [3, 4]))
edge.put((7, [1, 4]))
edge.put((6, [3, 5]))
edge.put((8, [4, 5]))
edge.put((9, [4, 6]))
edge.put((11, [5, 6]))


def kruskal(X, E):
    T = list()
    usedVertex = list(range(0, len(X)))
    while (len(T)) != (len(X) - 1):
        if E.qsize() == 0:
            return
        for i in range(0, E.qsize()):
            temp = E.get()
            if usedVertex[temp[1][0]] != usedVertex[temp[1][1]]:
                T.append(temp)
                t = min(usedVertex[temp[1][0]], usedVertex[temp[1][1]])
                m = max(usedVertex[temp[1][0]], usedVertex[temp[1][1]])
                for j in range(0, len(usedVertex)):
                    if (usedVertex[j] == m):
                        usedVertex[j] = t
                break
    print(T)


V = list(range(0, 7))
print("Các cạnh trong cây khung tối thiểu là: ")
kruskal(V, edge)
