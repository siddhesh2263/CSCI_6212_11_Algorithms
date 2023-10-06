import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection='3d')
ax.grid()

V = [4,6,8,10,12,14,16,18,20]

E = [6,
9,
12,
15,
18,
21,
24,
27,
30,]

experimental = [
0,
0.0957408553,
0.2039813022,
0.3215163606,
0.4464583384,
0.577559912,
0.7139345578,
0.8549194223,
1
]

theory = [
0,
0.139204199,
0.2598567677,
0.3377591996,
0.4819865918,
0.7136539967,
0.8926559974,
0.8865787516,
1
]

t_theory = np.array(V)
x_theory = np.array(E)
y_theory = np.array(theory)

t_experimental = np.array(V)
x_experimental = np.array(E)
y_experimental = np.array(experimental)

ax.plot3D(x_theory, y_theory, t_theory)
ax.plot3D(x_experimental, y_experimental, t_experimental)

ax.set_title('3D Parametric Plot')

# Set axes label
ax.set_xlabel('Edges', labelpad=20)
ax.set_ylabel('Normalized Theory/Experimental Values', labelpad=20)
ax.set_zlabel('Vertices ', labelpad=20)

plt.show()