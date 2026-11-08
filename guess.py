import random

answer = random.randint(1,100)
count = 0

while True:
    guess = int(input("猜一个1到100的数字："))
    count = count+1

    if guess == answer:
        print(f"猜对了！你用了{count}次")
        break
    elif guess > answer:
        print("大了")
    else:
        print("小了")

