def count_words(filename):
    counts = {}
    with open(filename, encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for w in words:
                w = w.lower().strip(".,!?;:\"'()")
                if w == "":
                    continue
                counts[w] = counts.get(w, 0) + 1
    return counts

try:
    counts = count_words("sample.txt")
except FileNotFoundError:
    print("找不到sample.txt，检查一下文件名和路径")
    exit()
print(f"不同单词数：{len(counts)}")

items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for word, c in items[:10]:
    print(f"{word}: {c}")