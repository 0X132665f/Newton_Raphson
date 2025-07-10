import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

fx = input("함수를 입력하세요 (예: x**2): ")

x0 = float(input("초기 추정 값을 입력하세요 (x 값): "))

x = sp.symbols('x')
expr = sp.sympify(fx)
f = sp.lambdify(x, expr, 'numpy')

# 도함수
dfExpr = sp.diff(expr, x)
df = sp.lambdify(x, dfExpr, 'numpy')

# 뉴턴
maxIter = 10
xNewton = [x0]

# for i in range(maxIter):
#     y = f(xNewton[-1])
#     dy = df(xNewton[-1])
#     xNext = xNewton[-1] - y / dy
#     xNewton.append(xNext)
#     if abs(xNext - xNewton[-2]) < 10 ** -2:
#         print(f"{i+1}번째 반복에서 수렴했습니다.")
#         break

cnt = 0
while(1):
    y = f(xNewton[-1])
    dy = df(xNewton[-1])
    xNext = xNewton[-1] - y / dy
    xNewton.append(xNext)
    cnt += 1
    if abs(xNext - xNewton[-2]) < 10 ** -2:
        print(f"{cnt}번째 반복에서 수렴했습니다.")
        break

# 수렴
if len(xNewton) >= 2:
    xTan = xNewton[-1]
    yTan = f(xTan)
    slopeTan = df(xTan)
    tangentX = np.linspace(xTan-3, xTan+3, 50)
    tangentY = slopeTan * (tangentX - xTan) + yTan

startX = xNewton[-1] - 6
endX = xNewton[-1] + 6

xVals = np.linspace(startX, endX, 300)
yVals = f(xVals)

plt.figure(figsize=(8, 6))
plt.plot(xVals, yVals, label=f"f(x) = {fx}", color='blue')

# y=0
plt.plot([startX, endX], [0, 0], '--', color='green', linewidth=1.5, label='y = 0')

for idx, xn in enumerate(xNewton):
    if startX <= xn <= endX:
        plt.plot(xn, f(xn), 'ro')
        plt.text(xn, f(xn), f"{idx}", color='blue')

# 최종도함수 
if len(xNewton) >= 2:
    plt.plot(tangentX, tangentY, '--', color='gray', linewidth=2, label='tangent')

plt.xlim(startX, endX)  # x축 범위: 근의 ±6

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.gca().set_aspect('auto')

print(f"뉴턴-랩슨 방법으로 찾은 근: {xNewton[-1]}")

plt.show()

