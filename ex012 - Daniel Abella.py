# 12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo.

valor2 = valorfinal = 0
valorinicial = int(input('Digite o valor para ser multiplicado na tabuada: '))
print()

for valor2 in range(11):
    valorfinal = valorinicial * valor2
    print('{} x {} = {}'.format(valorinicial, valor2, valorfinal))