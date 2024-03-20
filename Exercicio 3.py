#Faça um programa que verifique (usando if e else) se uma letra digitada é “F” ou “M”. Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido.

# Solicita ao usuário para digitar "M" para Masculino ou "F" para Feminino
a = input("Digite M para Masculino\n F para Feminino")

# Verifica se a entrada é "M" (Masculino)
if a == "M":
    # Se a entrada for "M", imprime "Sexo masculino"
    print("Sexo masculino")

# Se a entrada não for "M", verifica se é "F" (Feminino)
elif a == "F":
    # Se a entrada for "F", imprime "Sexo Feminino"
    print("Sexo Feminino")

# Se a entrada não for nem "M" nem "F", imprime "Sexo inváli
