import numpy as np

np.random.seed(42)

x = np.linspace(0, 10, 50)
noise = np.random.randn(50)
y = 2 * x + 3 + noise

n = len(x)
w = 0.0
b = 0.0
lr = 0.02

y_pred = w * x + b
error = y_pred - y
loss_before = (error ** 2).mean()

dw = 2 * (error * x).mean()
db = 2 * error.mean()

print(f"更新前: w = {w:.4f}, b = {b:.4f}, loss = {loss_before:.6f}")
print(f"梯度:  dw = {dw:.4f}, db = {db:.4f}")

w = w - lr * dw
b = b - lr * db

error_after = (w * x + b) - y
loss_after = (error_after ** 2).mean()
print(f"更新后: w = {w:.4f}, b = {b:.4f}, loss = {loss_after:.6f}")
