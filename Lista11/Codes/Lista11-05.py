with open("names.txt", "w+") as namesFile:
    with open("grades.txt", "w+") as gradesFile:
        qty = int(input("Qtd alunos: "))
        
        for x in range(qty):
            namesFile.write(input("Name: ") + ("\n" if x < qty - 1 else ""))
            
            grades = input("Notas: ").split()
            for y in range(len(grades)):
                gradesFile.write(grades[y] + (" " if y < len(grades) - 1 else ""))
            if x < qty - 1:
                gradesFile.write("\n")
        
        with open("names-grades.txt", "w") as finalFile:
            gradesFile.seek(0)
            namesFile.seek(0)
            listOfNames = [z.strip('\n') for z in namesFile.readlines()]
            for x in range(qty):
                listOfGrades = [float(y.strip('\n')) for y in gradesFile.readline().split()]
                sumOfGrades = 0.0
                for grade in listOfGrades:
                    sumOfGrades += grade
                finalFile.write(f"{listOfNames[x]} {(sumOfGrades / len(listOfGrades)):.2f}" + ('\n' if x < qty - 1 else ""))