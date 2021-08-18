head = tail = 0
node = 1

n = int(input())

if n == 1:
    print("{}".format(head))

if n == 2:
    print("{} {}".format(head, node))

if n < 46 and n > 2:
    print("{} {}".format(head, node), end=" ")
    for x in range(n - 2):
        tail = head + node
        head = node
        node = tail
        
        if x == (n - 3):
            print(tail)
        else:
            print(tail, end=" ")
    