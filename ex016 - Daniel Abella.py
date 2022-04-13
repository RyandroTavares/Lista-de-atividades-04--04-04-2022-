# 16 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input('Digite a quantidade de números: '))
maior = menor = soma = contagem = 0
print()

for i in range(quantidade):
    numero = int(input('Digite um número: '))
    soma += numero
    contagem += 1
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print()
print('A soma dos números da {}, o maior deles {} e o menor deles {}!'.format(soma, maior, menor))