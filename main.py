systems5 = 5
systems = systems5 / 2 - (int(systems5 / 2))
print(systems)

plane: complex = (-0.5) ** 0.5
print(plane)

cortege = tuple('hello, world!')
print(cortege[1:3])

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(name)         # Tom
print(age)          # 37
print(position)     # software developer
print(company)     # Google

tom = ("Tom", 37, "Google", "software developer")

# получем подкортеж с 1 по 3 элемента (не включая)
print(tom[1:3])  # (37, "Google")

# получем подкортеж с 0 по 3 элемента (не включая)
print(tom[:3])  # ("Tom", 37, "Google")

# получем подкортеж с 1 по послдений элемент
print(tom[1:])  # (37, "Google", "software developer")