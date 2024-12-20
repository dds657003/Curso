import math

def soma(num1, num2):
    somar = num1 + num2
    return somar

def subtracao(num1, num2):
    subtrair = num1 - num2
    return subtrair

def divisao(num1, num2):
    if num2 > 0:
        dividir = num1/num2
        return dividir

def multiplicacao(num1, num2):
    multipicar = num1 * num2
    return multipicar

def potenciacao(num1, num2):
    potencia = num1 ** num2
    return potencia

def raiz(num1):
    raizquadrada = math.sqrt(num1)
    return raizquadrada

def fatorial(num1):
    fatorializar = math.factorial(num1)
    return fatorializar

num1 = float(input("diga um numero: "))
num2 = float(input("diga outro: "))

while True:
    print(" calculadora ")
    print("1 somar")
    print("2 Subtrair")
    print("3 dividir")
    print("4 multiplicar")
    print("5 potenciar")
    print("6 raiz quadrada")
    print("7 fatorização")
    print("8 sair")
    operacao = int(input("oque deseja fazer? "))

    if operacao == 1:
        print(soma(num1, num2))
    elif operacao == 2:
        print(subtracao(num1, num2))
    elif operacao == 3:
        print(divisao(num1, num2))
    elif operacao == 4:
        print(multiplicacao(num1, num2))
    elif operacao == 5:
        print(potenciacao(num1, num2))
    elif operacao == 6:
        print(raiz(num1))
    elif operacao == 7:
        print(fatorial(num1))
    elif operacao == 8:
        break
    else:
        print("operação não encontrada")

