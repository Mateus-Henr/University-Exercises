from random import randint

qty = int(input("Qtd pessoas: "))
names, surnames, heights = [], [], []
a = open("names-age.txt", "w")

for x in range(qty):
    names.append(input("Name: "))
    surnames.append(input("Surname: "))
    heights.append(float(input("Height: ")))
    a.write(f"{names[x]} {surnames[x]} {randint(10, 50)} {heights[x]}" + 
            ("\n" if x < qty - 1 else ""))

a.close()