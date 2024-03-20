#2. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

# Solicita ao usuário para digitar um número e converte o valor para inteiro
a = int(input("digite um número"))

# Verifica se o número digitado é maior que zero
if a > 0:
    # Se o número for maior que zero, imprime que o número é positivo
    print("o número é positivo")
else:
    # Se o número não for maior que zero, imprime que o número é negativo
    print("o número é negativo")