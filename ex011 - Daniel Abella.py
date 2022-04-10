# 11 Altere o programa anterior para mostrar no final a soma dos números.

soma = 0
valorinicial = int(input('Digite o valor inicial: '))
valorfinal = int(input('Digite o valor final: '))
valorfinal = valorfinal + 1
print()

for i in range(valorinicial, valorfinal):
    print(i)
    soma = soma + i
print(soma)
