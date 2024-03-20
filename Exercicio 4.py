#Faça um programa que verifique (usando if e else) se uma letra digitada é vogal ou consoante.

# Solicita ao usuário que digite uma letra
a = input("Digite uma letra")

# Verifica se a letra digitada é 'a', 'e', 'i', 'o' ou 'u' (vogais)
if (a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u'):
    # Se a letra digitada for uma vogal, imprime "É uma vogal"
    print("É uma vogal")

# Se a letra digitada não for uma das vogais, imprime "não é uma vogal"
else:
    print("não é uma vogal")