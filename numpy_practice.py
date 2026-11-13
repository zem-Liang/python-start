import numpy as np

scores = np.array([88, 95, 72, 60, 45, 91, 78])

print("全部成绩：", scores)
print("最高分：", scores.max())
print("最低分：", scores.min())
print("平均分：", round(scores.mean(), 1))
print("人数：", scores.size)
print("及格人数：", (scores >= 60).sum())
print("及格率：", (scores >= 60).mean())
print("不及格名单：", scores[scores < 60])
print("优秀名单：", scores[scores >= 90])