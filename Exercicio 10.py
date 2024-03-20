#Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou “Boa Noite” ou “Valor inválido”, conforme o caso.

# Solicita ao usuário que insira o turno de estudo e armazena a entrada em 'a'
a = input("Olá... que turno você estuda? M - Matutino | V - Vespertino | N - Noturno: ")

# Verifica qual foi o turno inserido e imprime a saudação correspondente
if a == "m" or a == "M":
    print("Bom dia")
if a == "v" or a == "V":
    print("Boa tarde")
if a == "n" or a == "N":
    print("Boa noite")