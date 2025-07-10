# Newton-Raphson Method Visualizer

This project is a Python-based visual tool that applies the **Newton-Raphson method** to find the root of a nonlinear equation. It allows the user to input a custom function and visualize the iterative process leading to the root.

## 📌 Features
- User-defined function input (e.g., `x**2 - 2`, `sin(x) - x/2`, etc.)
- Custom initial guess input
- Iterative root-finding using Newton-Raphson
- Visual plot of the function with:
  - Iteration points labeled
  - Tangent line at the final root approximation

## 🧮 Dependencies
- `sympy` : symbolic math (for parsing and differentiating expressions)
- `numpy` : numerical calculations
- `matplotlib` : plotting graphs

## 🚀 Installation & Usage

### 1. Install Dependencies

```bash
pip install sympy numpy matplotlib
