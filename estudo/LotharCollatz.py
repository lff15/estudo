c0 = int(input("Qual o valor para c0: "))
steps = 0

while c0 != 1:
    if c0 <= 0:
        print("invalido")
        c0 = int(input("Qual o valor para c0: "))
    elif c0 % 2 == 0:
        c0 = c0 / 2
        steps += 1
        print(c0)
    else:
        c0 = 3*c0+1
        steps += 1
        print(c0)
print(f"passos: {steps}")