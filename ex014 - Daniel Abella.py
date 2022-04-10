# 14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

soma = 0
for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    soma = soma + numero
print(soma)