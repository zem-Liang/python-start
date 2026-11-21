import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(42)

x = np.linspace(0, 10, 50)
noise = np.random.randn(50)
y = 2 * x + 3 + noise

print("x的形状：", x.shape)
print("y的形状：", y.shape)
print("x前五个：", x[:5])
print("y前五个：", y[:5])

plt.figure(figsize=(8, 5))
plt.scatter(x, y, s=25, alpha=0.7, label="观测数据")
plt.plot(x, 2 * x + 3, color="red", linewidth=2, label="真实规律 y=2x+3")

plt.title("带噪声的线性数据")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("linear_data.png", dpi=150, bbox_inches="tight")
plt.show()