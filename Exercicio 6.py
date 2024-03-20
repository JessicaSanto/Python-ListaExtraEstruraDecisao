#Faça um programa que leia três números, verifique (usando if e else), e mostre o maior deles.

# Solicita ao usuário que insira o primeiro número e armazena o valor em 'a'
a = int(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número e armazena o valor em 'b'
b = int(input("Digite o segundo número: "))

# Solicita ao usuário que insira o terceiro número e armazena o valor em 'c'
c = int(input("Digite o terceiro número: "))

# Verifica se 'a' é maior que 'b' e 'c'
if a > b and a > c:
    # Se 'a' for o maior, imprime 'a'
    print(a)

# Se 'a' não for o maior, verifica se 'b' é maior que 'a' e 'c'
elif b > a and b > c:
    # Se 'b' for o maior, imprime 'b'
    print(b)

# Se 'a' e 'b' não forem os maiores, 'c' deve ser o maior
else:
    # Se 'c' for o maior, imprime 'c'
    print(c)