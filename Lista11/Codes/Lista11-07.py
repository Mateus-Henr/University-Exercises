IPfile = open("ips.txt", "r")
validFile = open("valid.txt", "w")
invalidFile = open("invalid.txt", "w")

for line in IPfile:
    isValid = True
    formatted = line.strip().split(".")
    for pos in range(len(formatted)):
        if pos == 0:
            if int(formatted[pos]) < 1 or int(formatted[pos]) > 255 or len(formatted) != 4:
                isValid = False
        else:
            if int(formatted[pos]) < 0 or int(formatted[pos]) > 255 or len(formatted) != 4:
                isValid = False
    if isValid:
        validFile.write(line)
    else:
        invalidFile.write(line)

IPfile.close()
validFile.close()
invalidFile.close()