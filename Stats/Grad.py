import numpy as np
import sympy as sp
import torch

# Finite Difference Method
def finite_difference(f, x, h=1e-2):
    return (f(x + h) - f(x - h)) / (2 * h)

f_numeric = lambda x: np.sin(x)  # Example function
x_numeric = np.pi
fd_result = finite_difference(f_numeric, x_numeric)
print("Finite Difference Approximation:", fd_result)

# Symbolic Differentiation with SymPy
x_sym = sp.symbols('x')
f_sym = sp.sin(x_sym)
df_sym = sp.diff(f_sym, x_sym)
print("Symbolic Derivative:", df_sym)

# Evaluating symbolic derivative at x = 1
df_sym_evaluated = df_sym.subs(x_sym, x_numeric).evalf()
print("Evaluated Symbolic Derivative:", df_sym_evaluated)

# Automatic Differentiation with PyTorch
x_torch = torch.tensor([x_numeric], dtype=torch.float64, requires_grad=True)
f_torch = torch.sin(x_torch)

f_torch.backward()
print("Automatic Differentiation (Torch) Derivative:", x_torch.grad.item())
