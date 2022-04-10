# 12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo.

valor2 = 0
valorfinal = 0
for valor2 in range(11):
    valorfinal = 5 * valor2
    print('{} x {} = {}'.format(5, valor2, valorfinal))