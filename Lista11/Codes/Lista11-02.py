from random import randint

names, surnames = [], []
file = open("name-age.txt", "w")

for x in range(20):
    names.append(input("Name: "))
    surnames.append(input("Surname: "))
    file.write(f"{names[x]} {surnames[x]} {randint(10, 50)}" + ("\n" if x < 19 else ""))

file.close()