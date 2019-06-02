salary = float (input())

if salary < 1000:
    salary = salary*1.30
    print("%.2f" %salary)

elif salary >= 1000 and salary <= 2000:
    salary = salary*1.10
    print("%.2f" %salary)

else:
    print("%.2f" %salary)