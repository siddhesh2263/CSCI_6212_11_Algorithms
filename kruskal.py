# Kruskal's algorithm in Python
import time

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        # for u, v, weight in result:
        #     print("%d - %d: %d" % (u, v, weight))


# input graph 1: V=4 and E=6
# print("Graph with V=4 and E=6")
# g = Graph(4)
# g.add_edge(0, 1, 12)
# g.add_edge(0, 3, 27)
# g.add_edge(0, 2, 35)
# g.add_edge(1, 3, 13)
# g.add_edge(1, 2, 21)
# g.add_edge(2, 3, 34)


# input graph 2: V=6 and E=9
# print("Graph with V=6 and E=9")
# g = Graph(6)
# g.add_edge(0, 1, 13)
# g.add_edge(0, 3, 22)
# g.add_edge(0, 2, 35)
# g.add_edge(1, 2, 11)
# g.add_edge(1, 3, 24)
# g.add_edge(2, 3, 36)
# g.add_edge(2, 4, 17)
# g.add_edge(4, 5, 29)
# g.add_edge(3, 4, 38)


#input graph 3: V=8 and E=12
# print("Graph with V=8 and E=12")
# g = Graph(8)
# g.add_edge(0, 2, 19)
# g.add_edge(0, 1, 24)
# g.add_edge(0, 3, 37)
# g.add_edge(2, 1, 12)
# g.add_edge(2, 3, 25)
# g.add_edge(1, 3, 38)
# g.add_edge(2, 5, 10)
# g.add_edge(3, 5, 26)
# g.add_edge(4, 6, 31)
# g.add_edge(6, 7, 13)
# g.add_edge(6, 5, 28)
# g.add_edge(5, 7, 39)


#input graph 4: V=10 and E=15
# print("Graph with V=10 and E=15")
# g = Graph(10)
# g.add_edge(0, 1, 13)
# g.add_edge(0, 2, 24)
# g.add_edge(1, 2, 32)
# g.add_edge(1, 3, 18)
# g.add_edge(1, 4, 26)
# g.add_edge(2, 4, 30)
# g.add_edge(4, 6, 16)
# g.add_edge(3, 6, 28)
# g.add_edge(3, 5, 31)
# g.add_edge(6, 8, 13)
# g.add_edge(5, 8, 20)
# g.add_edge(5, 7, 34)
# g.add_edge(7, 9, 11)
# g.add_edge(8, 9, 21)
# g.add_edge(7, 8, 32)

#input graph 5: V=12 and E=18
# print("Graph with V=12 and E=18")
# g = Graph(12)
# g.add_edge(0, 1, 11)
# g.add_edge(0, 2, 28)
# g.add_edge(1, 2, 30)
# g.add_edge(1, 3, 19)
# g.add_edge(2, 3, 22)
# g.add_edge(3, 4, 33)
# g.add_edge(3, 5, 10)
# g.add_edge(4, 5, 23)
# g.add_edge(4, 6, 37)
# g.add_edge(5, 10, 17)
# g.add_edge(10, 11, 24)
# g.add_edge(5, 11, 32)
# g.add_edge(5, 6, 14)
# g.add_edge(6, 8, 26)
# g.add_edge(6, 7, 35)
# g.add_edge(7, 8, 11)
# g.add_edge(7, 9, 25)
# g.add_edge(9, 5, 36)


# input graph 6: V=14 and E=21
# print("Graph with V=14 and E=21")
# g = Graph(14)
# g.add_edge(0, 5, 16)
# g.add_edge(0, 1, 27)
# g.add_edge(0, 3, 31)
# g.add_edge(1, 2, 12)
# g.add_edge(1, 4, 21)
# g.add_edge(4, 2, 30)
# g.add_edge(2, 7, 15)
# g.add_edge(4, 7, 28)
# g.add_edge(4, 6, 35)
# g.add_edge(3, 6, 13)
# g.add_edge(7, 9, 27)
# g.add_edge(7, 12, 33)
# g.add_edge(9, 12, 11)
# g.add_edge(9, 11, 28)
# g.add_edge(6, 11, 32)
# g.add_edge(6, 8, 19)
# g.add_edge(6, 5, 20)
# g.add_edge(5, 10, 34)
# g.add_edge(10, 13, 19)
# g.add_edge(11, 13, 24)
# g.add_edge(8, 13, 36)


# input graph 7: V=16 and E=24
# print("Graph with V=16 and E=24")
# g = Graph(16)
# g.add_edge(0, 3, 10)
# g.add_edge(0, 1, 26)
# g.add_edge(0, 2, 34)
# g.add_edge(3, 1, 14)
# g.add_edge(3, 6, 25)
# g.add_edge(2, 5, 39)
# g.add_edge(5, 6, 13)
# g.add_edge(6, 7, 22)
# g.add_edge(4, 7, 35)
# g.add_edge(7, 10, 18)
# g.add_edge(10, 9, 22)
# g.add_edge(6, 9, 37)
# g.add_edge(9, 8, 10)
# g.add_edge(5, 8, 28)
# g.add_edge(8, 11, 34)
# g.add_edge(11, 12, 11)
# g.add_edge(9, 12, 29)
# g.add_edge(10, 13, 36)
# g.add_edge(13, 15, 12)
# g.add_edge(12, 15, 23)
# g.add_edge(12, 14, 37)
# g.add_edge(14, 15, 11)
# g.add_edge(11, 14, 23)
# g.add_edge(1, 4, 31)


# input graph 8: V=18 and E=27
# print("Graph with V=18 and E=27")
# g = Graph(18)
# g.add_edge(0, 1, 19)
# g.add_edge(0, 4, 24)
# g.add_edge(0, 5, 39)
# g.add_edge(4, 8, 13)
# g.add_edge(4, 9, 28)
# g.add_edge(8, 12, 32)
# g.add_edge(8, 13, 17)
# g.add_edge(8, 5, 27)
# g.add_edge(12, 9, 36)
# g.add_edge(12, 17, 16)
# g.add_edge(12, 16,21)
# g.add_edge(16, 13, 35)
# g.add_edge(4, 1, 18)
# g.add_edge(17, 14, 25)
# g.add_edge(13, 10, 33)
# g.add_edge(9, 14, 15)
# g.add_edge(9, 6, 21)
# g.add_edge(11, 14, 32)
# g.add_edge(5, 10, 14)
# g.add_edge(1, 2, 20)
# g.add_edge(2, 3, 31)
# g.add_edge(2, 7, 16)
# g.add_edge(3, 7, 22)
# g.add_edge(3, 6, 30)
# g.add_edge(7, 11, 13)
# g.add_edge(11, 15, 24)
# g.add_edge(10, 15, 37)


# input graph 9: V=20 and E=30
print("Graph with V=20 and E=30")
g = Graph(20)
g.add_edge(0, 1, 14)
g.add_edge(0, 4, 25)
g.add_edge(0, 7, 33)
g.add_edge(4, 7, 16)
g.add_edge(7, 14, 22)
g.add_edge(7, 11, 38)
g.add_edge(11, 14, 17)
g.add_edge(14, 18, 21)
g.add_edge(18, 15, 39)
g.add_edge(15, 12, 11)
g.add_edge(12, 8, 22)
g.add_edge(12, 16, 35)
g.add_edge(8, 5, 13)
g.add_edge(8, 9, 22)
g.add_edge(5, 1, 34)
g.add_edge(5, 2, 17)
g.add_edge(1, 2, 25)
g.add_edge(2, 3, 36)
g.add_edge(5, 6, 18)
g.add_edge(3, 6, 29)
g.add_edge(6, 10, 30)
g.add_edge(6, 9, 11)
g.add_edge(10, 13, 24)
g.add_edge(9, 13, 33)
g.add_edge(13, 16, 16)
g.add_edge(13, 17, 27)
g.add_edge(16, 17, 38)
g.add_edge(19, 16, 10)
g.add_edge(19, 17, 29)
g.add_edge(19, 15, 30)


sum = 0
counter = 1000000
temp_counter = counter

while counter > 0:
    before_time_ns = time.time_ns()
    g.kruskal_algo()
    after_time_ns = time.time_ns()
    total_time_ns = after_time_ns - before_time_ns
    sum = sum + total_time_ns
    counter = counter - 1

avg = sum / temp_counter

print("AVG: ", avg)

# before_time_ns = time.time_ns()
# g.kruskal_algo()
# after_time_ns = time.time_ns()
# total_time_ns = after_time_ns - before_time_ns

# print("Total  time in nanoseconds:", total_time_ns)