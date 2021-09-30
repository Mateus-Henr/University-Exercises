file = open("thisfile.txt", "w")

for i in range(200, 49, -1):
    file.write(f"{i}\n")

file.close()