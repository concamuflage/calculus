import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Math


x, y = sp.symbols('x y')

left = sp.exp(x**2 + y**2)
right = x + y

eq = sp.Eq(left, right)

# -------------------------
# Implicit derivative dy/dx
# -------------------------

implicit_derivative = sp.idiff(eq.lhs - eq.rhs, y, x)

display(Math(
    r'\frac{dy}{dx} = %s'
    % sp.latex(implicit_derivative)
))

# -------------------------
# Grid search
# -------------------------

# 10000 x 10000 is enormous.
# Start with something much smaller.
x_bouund = 0.5
y_bound =2
n = 1000
xx = np.linspace(-x_bouund, x_bouund, n)
yy = np.linspace(-y_bound, y_bound,  n)

X, Y = np.meshgrid(xx, yy)

exp = left - right
exp_num = sp.lambdify((x, y), exp, 'numpy')
exp_values = exp_num(X, Y)

eta = 0.0001

# Points approximately satisfying the implicit equation
curve_mask = np.abs(exp_values) < eta


plt.plot(
    X[curve_mask],
    Y[curve_mask],
    "k.",
    markersize=1
)

# -------------------------
# Derivative
# -------------------------

implicit_derivative_num = sp.lambdify(
    (x, y),
    implicit_derivative,
    'numpy'
)

derivative_values = implicit_derivative_num(X, Y)

# derivative ≈ 0 AND point lies on implicit curve
critical_mask = (
    # (np.abs(exp_values) < eta)
    # &
    (np.abs(derivative_values) < eta)
)

plt.plot(
    X[critical_mask],
    Y[critical_mask],
    "r+",
    markersize=10
)

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()