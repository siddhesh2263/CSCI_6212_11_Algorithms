import math as math

# E log V
# E = 3/2 V

V = [4, 6, 8, 10, 12, 14, 16, 18, 20]

E = [6,
9,
12,
15,
18,
21,
24,
27,
30,]

theory = []

for x in V:
    E = (3/2) * x
    theory_val = E * math.log(x, 2)
    theory.append(theory_val)

experimental = [
3012.6816,
4619.723,
6012.5953,
6911.9391,
8576.9707,
11251.4526,
13317.9393,
13247.7806,
14557.171
]

# x_changed = (x - x_min)/(x_max - x_min)

theory_normalized = []
expiremental_normalized = []

for x in V:
    min_val = min(V)
    max_val = max(V)
    x_changed = (x - min_val) / (max_val - min_val)
    theory_normalized.append(x_changed)

for x in E:
    min_val = min(E)
    max_val = max(E)
    x_changed = (x - min_val) / (max_val - min_val)
    expiremental_normalized.append(x_changed)

for x in theory_normalized:
    print(x)

print("----")

for x in expiremental_normalized:
    print(x)