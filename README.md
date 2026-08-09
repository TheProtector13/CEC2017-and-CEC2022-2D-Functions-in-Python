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
  - **CEC2017:** _U_C17_10 &harr; U_C17_19 | U_C17_28 &harr; U_C17_29_
  - **CEC2022:** _U_C22_6 &harr; U_C22_8_
- Adjusted CEC2022 composite functions to match the surface plots in the paper (unofficial; uses different sigma and lambda values)
  - _C22_9_Alt &harr; C22_12_Alt_

> [!TIP]
> The functions and their optimal values can also be accessed via arrays! <br><br>
> F.CEC2017 | F.CEC2017_Opts - Official CEC2017 functions <br>
> F.CEC2017_Unofficial | F.CEC2017_Unofficial_Opts - Unofficial CEC2017 functions <br>
> F.CEC2022 | F.CEC2022_Opts - Official CEC2022 functions <br>
> F.CEC2022_Alt | F.CEC2022_Alt_Opts - Adjusted CEC2022 composite functions <br>
> F.CEC2022_Unofficial | F.CEC2022_Unofficial_Opts - Unofficial CEC2022 functions <br>
> F.AllFunctions | F.AllOpts - All official functions (CEC2017+CEC2022) <br>
> F.AllFunctionsWithU | F.AllOptsWithU - All official, adjusted and unofficial functions <br>

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
# Function landscapes

<table width="100%">
  <tr>
    <th align="left">Function</th>
    <th align="center">3D Surface</th>
    <th align="center">Landscape Contour</th>
  </tr>

  <tr>
    <td><b>C17_1</b></td>
    <td><img src="FIG_Output/1_C17_1.png" width="100%"></td>
    <td><img src="FIG_Output/1_C17_1_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_2</b></td>
    <td><img src="FIG_Output/2_C17_2.png" width="100%"></td>
    <td><img src="FIG_Output/2_C17_2_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_3</b></td>
    <td><img src="FIG_Output/3_C17_3.png" width="100%"></td>
    <td><img src="FIG_Output/3_C17_3_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_4</b></td>
    <td><img src="FIG_Output/4_C17_4.png" width="100%"></td>
    <td><img src="FIG_Output/4_C17_4_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_5</b></td>
    <td><img src="FIG_Output/5_C17_5.png" width="100%"></td>
    <td><img src="FIG_Output/5_C17_5_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_6</b></td>
    <td><img src="FIG_Output/6_C17_6.png" width="100%"></td>
    <td><img src="FIG_Output/6_C17_6_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_7</b></td>
    <td><img src="FIG_Output/7_C17_7.png" width="100%"></td>
    <td><img src="FIG_Output/7_C17_7_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_8</b></td>
    <td><img src="FIG_Output/8_C17_8.png" width="100%"></td>
    <td><img src="FIG_Output/8_C17_8_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_9</b></td>
    <td><img src="FIG_Output/9_C17_9.png" width="100%"></td>
    <td><img src="FIG_Output/9_C17_9_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_20</b></td>
    <td><img src="FIG_Output/10_C17_20.png" width="100%"></td>
    <td><img src="FIG_Output/10_C17_20_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_21</b></td>
    <td><img src="FIG_Output/11_C17_21.png" width="100%"></td>
    <td><img src="FIG_Output/11_C17_21_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_22</b></td>
    <td><img src="FIG_Output/12_C17_22.png" width="100%"></td>
    <td><img src="FIG_Output/12_C17_22_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_23</b></td>
    <td><img src="FIG_Output/13_C17_23.png" width="100%"></td>
    <td><img src="FIG_Output/13_C17_23_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_24</b></td>
    <td><img src="FIG_Output/14_C17_24.png" width="100%"></td>
    <td><img src="FIG_Output/14_C17_24_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_25</b></td>
    <td><img src="FIG_Output/15_C17_25.png" width="100%"></td>
    <td><img src="FIG_Output/15_C17_25_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_26</b></td>
    <td><img src="FIG_Output/16_C17_26.png" width="100%"></td>
    <td><img src="FIG_Output/16_C17_26_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C17_27</b></td>
    <td><img src="FIG_Output/17_C17_27.png" width="100%"></td>
    <td><img src="FIG_Output/17_C17_27_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_10</b></td>
    <td><img src="FIG_Output/18_U_C17_10.png" width="100%"></td>
    <td><img src="FIG_Output/18_U_C17_10_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_11</b></td>
    <td><img src="FIG_Output/19_U_C17_11.png" width="100%"></td>
    <td><img src="FIG_Output/19_U_C17_11_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_12</b></td>
    <td><img src="FIG_Output/20_U_C17_12.png" width="100%"></td>
    <td><img src="FIG_Output/20_U_C17_12_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_13</b></td>
    <td><img src="FIG_Output/21_U_C17_13.png" width="100%"></td>
    <td><img src="FIG_Output/21_U_C17_13_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_14</b></td>
    <td><img src="FIG_Output/22_U_C17_14.png" width="100%"></td>
    <td><img src="FIG_Output/22_U_C17_14_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_15</b></td>
    <td><img src="FIG_Output/23_U_C17_15.png" width="100%"></td>
    <td><img src="FIG_Output/23_U_C17_15_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_16</b></td>
    <td><img src="FIG_Output/24_U_C17_16.png" width="100%"></td>
    <td><img src="FIG_Output/24_U_C17_16_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_17</b></td>
    <td><img src="FIG_Output/25_U_C17_17.png" width="100%"></td>
    <td><img src="FIG_Output/25_U_C17_17_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_18</b></td>
    <td><img src="FIG_Output/26_U_C17_18.png" width="100%"></td>
    <td><img src="FIG_Output/26_U_C17_18_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_19</b></td>
    <td><img src="FIG_Output/27_U_C17_19.png" width="100%"></td>
    <td><img src="FIG_Output/27_U_C17_19_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_28</b></td>
    <td><img src="FIG_Output/44_U_C17_28.png" width="100%"></td>
    <td><img src="FIG_Output/44_U_C17_28_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C17_29</b></td>
    <td><img src="FIG_Output/45_U_C17_29.png" width="100%"></td>
    <td><img src="FIG_Output/45_U_C17_29_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_1</b></td>
    <td><img src="FIG_Output/28_C22_1.png" width="100%"></td>
    <td><img src="FIG_Output/28_C22_1_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_2</b></td>
    <td><img src="FIG_Output/29_C22_2.png" width="100%"></td>
    <td><img src="FIG_Output/29_C22_2_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_3</b></td>
    <td><img src="FIG_Output/30_C22_3.png" width="100%"></td>
    <td><img src="FIG_Output/30_C22_3_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_4</b></td>
    <td><img src="FIG_Output/31_C22_4.png" width="100%"></td>
    <td><img src="FIG_Output/31_C22_4_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_5</b></td>
    <td><img src="FIG_Output/32_C22_5.png" width="100%"></td>
    <td><img src="FIG_Output/32_C22_5_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_9</b></td>
    <td><img src="FIG_Output/33_C22_9.png" width="100%"></td>
    <td><img src="FIG_Output/33_C22_9_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_10</b></td>
    <td><img src="FIG_Output/34_C22_10.png" width="100%"></td>
    <td><img src="FIG_Output/34_C22_10_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_11</b></td>
    <td><img src="FIG_Output/35_C22_11.png" width="100%"></td>
    <td><img src="FIG_Output/35_C22_11_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_12</b></td>
    <td><img src="FIG_Output/36_C22_12.png" width="100%"></td>
    <td><img src="FIG_Output/36_C22_12_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_9_Alt</b></td>
    <td><img src="FIG_Output/37_C22_9_Alt.png" width="100%"></td>
    <td><img src="FIG_Output/37_C22_9_Alt_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_10_Alt</b></td>
    <td><img src="FIG_Output/38_C22_10_Alt.png" width="100%"></td>
    <td><img src="FIG_Output/38_C22_10_Alt_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_11_Alt</b></td>
    <td><img src="FIG_Output/39_C22_11_Alt.png" width="100%"></td>
    <td><img src="FIG_Output/39_C22_11_Alt_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>C22_12_Alt</b></td>
    <td><img src="FIG_Output/40_C22_12_Alt.png" width="100%"></td>
    <td><img src="FIG_Output/40_C22_12_Alt_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C22_6</b></td>
    <td><img src="FIG_Output/41_U_C22_6.png" width="100%"></td>
    <td><img src="FIG_Output/41_U_C22_6_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C22_7</b></td>
    <td><img src="FIG_Output/42_U_C22_7.png" width="100%"></td>
    <td><img src="FIG_Output/42_U_C22_7_contour.png" width="100%"></td>
  </tr>

  <tr>
    <td><b>U_C22_8</b></td>
    <td><img src="FIG_Output/43_U_C22_8.png" width="100%"></td>
    <td><img src="FIG_Output/43_U_C22_8_contour.png" width="100%"></td>
  </tr>

</table>

## Sources:
- CEC2017 - [link](https://github.com/P-N-Suganthan/CEC2017-BoundContrained)
- CEC2022 - [link](https://github.com/P-N-Suganthan/2022-SO-BO)
