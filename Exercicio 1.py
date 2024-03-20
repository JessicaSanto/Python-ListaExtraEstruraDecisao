#1. Faça um programa que peça dois números e verifique (usando if e else) e imprima o maior deles

# Solicita ao usuário para digitar o primeiro número e armazena o valor em 'a'
a = input("digite o primeiro numero")

# Solicita ao usuário para digitar o segundo número e armazena o valor em 'b'
b = input("digite o segundo número")

# Verifica se o valor armazenado em 'b' é maior que o valor em 'a'
if b > a:
    # Se 'b' for maior que 'a', imprime 'b'
    print(b)
else:
    # Se 'b' não for maior que 'a', imprime 'a'
    print(a)