num1 = int(input("Input your 1st number: "))
num2 = int(input("Input your 2nd number: "))
num3 = int(input("Input your 3rd number: "))
if num1 > num2 > num3 :
    print("1st num is the most")
elif num2 > num1 > num3:
    print('2nd num is the most')
elif num3 > num2 > num1:
    print('3rd num is the most')
else:
    pass

