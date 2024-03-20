#Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor

# Solicita ao usuário que insira o primeiro número e armazena o valor em 'num1'
num1 = input("Digite o primeiro número: ")

# Solicita ao usuário que insira o segundo número e armazena o valor em 'num2'
num2 = input("Digite o segundo número: ")

# Verifica qual é o maior número entre 'num1' e 'num2'
if num1 > num2:
    # Se 'num1' for maior que 'num2', imprime 'num1' como o maior e 'num2' como o menor
    print("O maior é:", num1)
    print("O menor é:", num2)
else:
    # Se 'num2' for maior que ou igual a 'num1', imprime 'num2' como o maior e 'num1' como o menor
    print("O maior é:", num2)
    print("O menor é:", num1)