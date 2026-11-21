import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 10, 100)

plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label="sin(x)", color="tab:blue")
plt.plot(x, np.cos(x), label="cos(x)", color="tab:orange", linestyle="--")

plt.title("正弦与余弦")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("sin_cos.png", dpi=150, bbox_inches="tight")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.randn(100)
# y = np.random.randn(100)

# plt.scatter(x, y, s=20, alpha=0.6)
# plt.show()