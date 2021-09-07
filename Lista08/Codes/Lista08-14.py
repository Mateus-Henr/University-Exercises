a, mai = [[int(input(f"{i + 1}° del | {j + 1}° atlet - Altura: ")) for j in range(10)] for i in range(5)], []

for x in range(len(a)):
    mai.append(a[x][0])
    for y in a[x]:
        if y > mai[x]: mai[x] = y
    
[print(f"Maior {x + 1}° del - altura {mai[x]}m") for x in range(5)]