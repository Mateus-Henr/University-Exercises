strings = [input(f"{x + 1}° string: ") for x in range(2)]
palin = True

if len(strings[0]) == len(strings[1]):
    for x in range(len(strings[0])):
      if strings[0][x] != strings[1][len(strings[1]) - x - 1]: palin = False
else: palin = False

print("São palí­ndromas" if palin else "Não são palí­ndromas")