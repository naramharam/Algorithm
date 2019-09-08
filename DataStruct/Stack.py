def stack():
    stack = []
    for i in range(0, 7):
        stack.append(i)
    print(stack)

    while stack:
       print("POP->", stack.pop())


stack()