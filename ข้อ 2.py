num = float(input("Input yur number:"))

if num > 0:
    output = 'เลขบวก'
elif num==0:
    output = "เลขศูนย์"
elif num < 0:
    output = "เลขลบ"
else :
    print("Error")
print(output)
