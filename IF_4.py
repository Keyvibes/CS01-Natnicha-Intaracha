score1 = float(input("Input your summative scores :"))
if score1 > 30:
    print("Error, type again")
    quit()
score2 = float(input("Input your midterm scores :"))
if score2 > 30:
    print("Error, type again")
    quit()
score3 = float(input("Input your final scores :"))
if score3 > 40:
    print("Error, type again")
    quit()
all = (score1+score2+score3)
if all >=80:
    grade = "A"
elif all >=75:
    grade = "B+" 
elif all >=70:
    grade = "B"
elif all >=65:
    grade = "C+"
elif all >=60:
    grade = "c"
elif all >=55:
    grade = "D+"
elif all >=50:
    grade = "D"
else :
    grade = "F"

print("Your grade is",grade)


