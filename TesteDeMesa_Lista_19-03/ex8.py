lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))
lado4 = int(input("Digite o valor do lado 4: "))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3 and lado3 == lado4:
    print("É um quadrado")
elif (lado1 == lado2 and lado3 == lado4) or (lado1 == lado4 and lado2 == lado3) or (lado1 == lado3 and lado2 == lado4):
    print("É um retêngulo")
else:
    print("Não é um quadrado e nem um retângulo")