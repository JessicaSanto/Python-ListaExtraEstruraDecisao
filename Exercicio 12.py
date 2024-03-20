#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1- Domingo , 2- Segunda, etc.) se digitar outro valor deve aparecer “valor inválido)

# Solicita ao usuário que insira um número e converte o valor para um número inteiro
num = int(input("Digite um número: "))

# Verifica qual é o número inserido e imprime o dia da semana correspondente
if num == 1:
    print("Domingo")
if num == 2:
    print("Segunda-feira")
if num == 3:
    print("Terça-feira")
if num == 4:
    print("Quarta-feira")
if num == 5:
    print("Quinta-feira")
if num == 6:
    print("Sexta-feira")
if num == 7:
    print("Sábado")