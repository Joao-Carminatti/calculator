print("Esse programa será uma calculadora!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def soma(num1, num2):
    adicao = num1 + num2
    return f"O resultado da soma de {num1} + {num2} é igual a {adicao}"

def subtracao(num1, num2):
    menos = num1 - num2
    return f"A subtração de {num1} - {num2} é igual a {menos}"

def multiplicacao(num1, num2):
    vezes = num1 * num2
    return f"A multiplicação de {num1} x {num2} é igual a {vezes}"

def divisao(num1, num2):
    divide = num1 / num2
    return f"A Divisão de {num1} / {num2} é igual a {divide}"

opcao = int(input("Digite qual operação deseja realizar:\n1)Soma\n2)Subtração\n3)Multiplicação\n4)Divisão\n:"))

match opcao:
    case 1:
        print(soma(num1, num2))
    case 2:
        print(subtracao(num1, num2))
    case 3:
        print(multiplicacao(num1, num2))
    case 4:
        print(divisao(num1, num2))
    case other:
        print("Você não digitou nenhuma opção disponivel!")
