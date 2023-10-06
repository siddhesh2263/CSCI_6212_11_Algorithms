# E = 4/3 * V

import math as math

V = [4,6,8,10,12,14,16,18,20]

theory = []

for x in V:
    E = (3/2) * x
    print(E)
    theory_val = E * math.log(x, 2)
    theory.append(theory_val)

print("----")

for x in theory:
    print(x)

# theory_base_10 = []

# for x in theory:
#     base_10_val = math.log(x, 10)
#     theory_base_10.append(base_10_val)