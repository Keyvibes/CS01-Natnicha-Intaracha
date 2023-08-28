sum = 0
for i in range(10):
    num = int(input("Input your number: "))
    if num < 0:
        continue
    sum += num
print("Answer:", sum)