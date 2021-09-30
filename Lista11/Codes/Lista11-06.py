namesFile = open("names.txt", "r")
gradesFile = open("grades.txt", "r+")
finalFile = open("names-grades.txt", "w+")

name, grade = input("Name: "), float(input("Old grade: "))
newGrade = float(input("New grade: "))

names, grades = [x.strip('\n') for x in namesFile.readlines()], []
for x in range(len(names)):
    grades.append([float(y) for y in gradesFile.readline().split()])

if name in names:
    idx = names.index(name)
    if grade in grades[idx]:
        finalFile.seek(0)
        gradesFile.seek(0)
        grades[idx][grades[idx].index(grade)] = newGrade
        for x in range(len(grades)):
            for y in range(len(grades[x])):
                gradesFile.write(str(grades[x][y]) + 
                                 (" " if y < len(grades[x]) - 1 else ""))
            if x < len(grades) - 1: gradesFile.write("\n")
            finalFile.write(f"{names[x]} {(sum(grades[x]) / len(grades[x])):.2f}" 
                            + ("\n" if x < len(grades) - 1 else ""))
    else: print("Grade not found.")
                
namesFile.close()
gradesFile.close()
finalFile.close()