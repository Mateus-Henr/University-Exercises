total = 0
x = int(input())
y = int(input())

if x > y:
    temp = x
    x = y
    y = temp
    
for n in range(x, y + 1):
    if n % 13 != 0:
        total += n

print(str(total))