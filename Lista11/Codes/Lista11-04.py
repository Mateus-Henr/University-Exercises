file = open("file.txt", "r")
copiedFile = open("copiedFile.txt", "w")

for line in file:
   if line.strip()[0:2] != "//":
       copiedFile.write(line)

file.close()
copiedFile.close()