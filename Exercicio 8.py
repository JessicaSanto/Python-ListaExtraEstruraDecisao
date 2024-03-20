#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato.

# Solicita ao usuário que insira o preço do primeiro produto e armazena o valor em 'a'
a = int(input("Digite o preço do primeiro produto: "))

# Solicita ao usuário que insira o preço do segundo produto e armazena o valor em 'b'
b = int(input("Digite o preço do segundo produto: "))

# Solicita ao usuário que insira o preço do terceiro produto e armazena o valor em 'c'
c = int(input("Digite o preço do terceiro produto: "))

# Inicializa a variável 'menor' com um valor arbitrário
# Este valor será substituído posteriormente pelo valor do produto com menor preço
menor = 0

# Verifica qual é o menor preço entre 'a', 'b' e 'c'
if a < b and a < c :
    menor =  a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Imprime o produto com o menor preço
print("O melhor produto para você é: ", menor)