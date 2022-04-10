# 07 Faça um programa que leia 5 números e informe o maior número.

numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número: ")))

maior = numeros[0]

contagem = 1
while contagem < len(numeros):
    if numeros[contagem] > maior:
        maior = numeros[contagem]
    contagem = contagem + 1
        
print()
print ("O maior número é o {}".format(maior))