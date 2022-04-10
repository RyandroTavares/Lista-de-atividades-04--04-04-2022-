# 10 Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

valorinicial = int(input('Digite o valor inicial: '))
valorfinal = int(input('Digite o valor final: '))
valorfinal = valorfinal + 1
print()

for i in range(valorinicial, valorfinal):
    print(i)
