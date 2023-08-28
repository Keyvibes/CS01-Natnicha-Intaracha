num1 = float(input("input num1: "))
num2 = float(input("input num2: "))

def add_numbers(a, b):
    result = a + b
    return result


sum_result = add_numbers(num1, num2)
print("The answer of", num1, "and", num2, "is", sum_result)