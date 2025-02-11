def calculadora(num1, num2, op) :
    if op == "soma":
        return num1 + num2
    elif op == "subtração":
        return num1 - num2
    elif op == "multiplicação":   
        return num1 * num2
    elif op == "divisão":
        return num1 / num2
    else:
        return "Essa operação não existe"


while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    op = input("Digite a operação: ")
    print(calculadora(num1, num2, op))
    continuar = input("Deseja continuar? (s/n) ")
    if continuar == "n":
        break

