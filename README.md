# CEC2017-and-CEC2022-2D-Functions-in-Python
A Python implementation of the CEC 2017 and CEC 2022 single objective optimization benchmark functions. The package currently provides only two-dimensional (2D) implementations.

> [!IMPORTANT]
> Due to instability, the second benchmark function was excluded from the CEC2017 implementation, resulting in an index shift of one for all subsequent functions.
> The indexing is based on the paper: Problem Definitions and Evaluation Criteria for the CEC 2017 Special Session and Competition on Single Objective Real-Parameter Numerical Optimization. [Link](https://www.scribd.com/document/546719948/Definitions-of-CEC2017-benchmark-suite-final-version-updated)

## Importing module
```python
from Functions import Functions
```

## Creating an instance
```python
F = Functions()
```

## Available benchmark functions
- Official functions (Functions natively defined in 2D according to the original paper):
  - **CEC2017:** _C17_1 &harr; C17_9 | C17_20 &harr; C17_27_
  - **CEC2022:** _C22_1 &harr; C22_5 | C22_9 &harr; C22_12_
- Unofficial functions (Higher-dimensional functions adapted for 2D inputs; Hybrid functions)
  - **CEC2017:** _U_C17_10 &harr; U_C17_19_
  - **CEC2022:** _U_C22_6 &harr; U_C22_8_
- Adjusted CEC2022 composite functions to match the surface plots in the paper (unofficial; uses different sigma and lambda values)
  - _C22_9_Alt &harr; C22_12_Alt_

> [!TIP]
> The functions and their optimal values can also be accessed via arrays!
> F.CEC2017 | F.CEC2017_Opts - Official CEC2017 functions
> F.CEC2017_Unofficial | F.CEC2017_Unofficial_Opts - Unofficial CEC2017 functions
> F.CEC2022 | F.CEC2022_Opts - Official CEC2022 functions
> F.CEC2022_Alt | F.CEC2022_Alt_Opts - Adjusted CEC2022 composite functions
> F.CEC2022_Unofficial | F.CEC2022_Unofficial_Opts - Unofficial CEC2022 functions
> F.AllFunctions | F.AllOpts - All official functions (CEC2017+CEC2022)
> F.AllFunctionsWithU | F.AllOptsWithU - All official, adjusted and unofficial functions

## Usage
```python
# Specifying X and Y coordinates in the -100 <= x <= 100 search range
X = 10
Y = -20

# Determining Z axis value with the selected benchmark function
Z = F.C17_3(X, Y)
print(Z)

# Getting the global optimum value for the specific function
optimum = F.C17_3_Opt
print(optimum)

# Getting the difference between the global optimum and the calculated value Z (absolute error)
Err = abs(Z - optimum)
print(Err)
```

### Plotting the function landscape over the full search space
```python
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from Functions import Functions

F = Functions()

x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)
X, Y = np.meshgrid(x, y)
Z = np.empty_like(X)

for i in range(len(X[0])):
    for j in range(len(X[0])):
        Z[i,j] = F.C22_2(X[i,j],Y[i,j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='plasma')
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.xaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.yaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.zaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))

ax.set_facecolor((1.0, 1.0, 1.0, 0.0))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.grid(True)
# contour

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
cf = ax2.contourf(X, Y, Z, levels=200, cmap='viridis')
cs = ax2.contour(X, Y, Z, levels=15, cmap='autumn', linewidths=0.5)
fig2.colorbar(cf)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect('equal')
fig2.show()

print(np.max(Z))

plt.show()
```

## Sources:
- CEC2017 - [link](https://github.com/P-N-Suganthan/CEC2017-BoundContrained)
- CEC2022 - [link](https://github.com/P-N-Suganthan/2022-SO-BO)
