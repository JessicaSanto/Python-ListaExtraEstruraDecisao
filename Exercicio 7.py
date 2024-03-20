#Faça um programa que leia três números, verifique (usando if e else) e mostre o maior e o menor deles;

# Solicita ao usuário que insira o primeiro número e armazena o valor em 'a'
a = int(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número e armazena o valor em 'b'
b = int(input("Digite o segundo número: "))

# Solicita ao usuário que insira o terceiro número e armazena o valor em 'c'
c = int(input("Digite o terceiro número: "))

# Inicializa as variáveis 'maior' e 'menor' com valores arbitrários
# Estes valores serão substituídos posteriormente pelos valores reais dos números inseridos pelo usuário
maior = 0
menor = 0

# Verifica qual é o maior número entre 'a', 'b' e 'c'
if a > b and a > c :
    maior =  a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

# Verifica qual é o menor número entre 'a', 'b' e 'c'
if a < b and a < c :
    menor =  a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Imprime o maior e o menor números
print(maior, menor)