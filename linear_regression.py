import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(42)

x = np.linspace(0, 10, 50)
noise = np.random.randn(50)
y = 2 * x + 3 + noise

n = len(x)
w = 0.0
b = 0.0
lr = 0.02
epochs = 500

losses = []

for epoch in range(epochs):
    y_pred = w * x + b
    error = y_pred - y

    loss = (error ** 2).mean()
    losses.append(loss)

    dw = 2 * (error * x).mean()
    db = 2 * error.mean()

    w = w - lr * dw
    b = b - lr * db

print(f"学到的参数: w = {w:.4f}, b = {b:.4f}")
print(f"初始 loss: {losses[0]:.6f}")
print(f"最终 loss: {losses[-1]:.6f}")
print(f"真实参数: w = 2.0000, b = 3.0000")

plt.figure(figsize=(8, 5))
plt.plot(losses, color="tab:blue")
plt.title("训练损失曲线")
plt.xlabel("epoch")
plt.ylabel("loss (MSE)")
plt.grid(alpha=0.3)
plt.savefig("loss_curve.png", dpi=150, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(x, y, s=25, alpha=0.7, label="观测数据")
plt.plot(x, w * x + b, color="red", linewidth=2, label=f"拟合: y = {w:.2f}x + {b:.2f}")
plt.title("线性回归拟合结果")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("fit_result.png", dpi=150, bbox_inches="tight")
plt.show()
