s1, s2 = [input(f"{x + 1}� string: ").strip() for x in range(2)]
isAnagrama = True

if len(s1) == len(s2):
    for x in s1:
        if x.lower() not in s2.lower():
            isAnagrama = False
else: isAnagrama = False

print("S�o anagramas." if isAnagrama else "N�o s�o anagramas.")