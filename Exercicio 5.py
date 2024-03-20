#Faça um programa para a leitura de duas notas parciais de um aluno.

#- A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#- A mensagem “Aprovado com Distinção”, se a média for igual a dez;
#- A mensagem “Reprovado” se a média for menor de do que sete;

# Solicita ao usuário que insira a nota da primeira parcial e a armazena em 'parcial1'
parcial1 = int(input("Digite a nota da primeira parcial: "))

# Solicita ao usuário que insira a nota da segunda parcial e a armazena em 'parcial2'
parcial2 = int(input("Digite a nota da segunda parcial: "))

# Calcula a média das duas parciais
media = (parcial1 + parcial2) / 2

# Verifica se a média é igual a 10
if media == 10:
    # Se a média for igual a 10, imprime "Aprovado com distinção"
    print("Aprovado com distinção")

# Se a média não for igual a 10, verifica se é maior ou igual a 7
elif media >= 7:
    # Se a média for maior ou igual a 7, imprime "Aprovado"
    print("Aprovado")

# Se a média não for nem igual a 10 nem maior ou igual a 7, imprime "Reprovado"
else:
    print("Reprovado")