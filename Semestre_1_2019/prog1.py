#basesalary
basesalary = float(input("Insira o salario base:"))
bonus = 50
tax = basesalary * 0.12
tot = ((basesalary - tax) + bonus )

print("Seu salario base é: ", basesalary)
print("Seu bonus é: ", bonus)
print("A taxa é : ", tax)
print("O total é : ", tot)