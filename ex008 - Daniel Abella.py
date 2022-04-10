# 08 Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
media = 0
for i in range(5):
    numero = int(input('Digite um valor: '))
    soma = soma + numero
media = soma / 5

print('A soma das notas é {} e a média é de {}'.format(soma, media))