# 01 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 11
while nota < 0 or nota > 10:
    nota = int(input('Digite uma nota entre 0 a 10 para sair: '))
    print('Você digitou a nota', nota)
    print()

print('Saindo...')