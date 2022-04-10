# 03 Faça um programa que leia e valide as seguintes informações:
# • Nome: maior que 3 caracteres;
# • Idade: entre 0 e 150;
# • Salário: maior que zero;
# • Sexo: 'f' ou 'm';
# • Estado Civil: 's', 'c', 'v', 'd’;

nome = input('Digite um nome maior que 3 caracteres: ').upper()
while len(nome) <= 3:
    print('Error, tente novamente!')
    print()
    nome = input('Digite um nome maior que 3 caracteres: ').upper()
print()

idade = int(input('Digite uma idade entre 0 a 150: '))
while idade < 150:
    print('Error, tente novamente!')
    print()
    idade = int(input('Digite uma idade entre 0 a 150: '))
print()

salario = int(input('Digite o seu salário: '))
while salario < 1:
    print('Error, tente novamente!')
    print()
    salario = int(input('Digite o seu salário: '))
print()

sexo = input('Digite o seu sexo: ').upper()
while sexo != 'F' and sexo != 'M':
    print('Error, tente novamente!')
    print()
    sexo = input('Digite o seu sexo: ').upper()
print()

estadocivil = input('Digite seu estado Civil: (S - Solteiro, C - Casado, V - Viúvo e D - Divorciado) ').upper()
while estadocivil != 'S' and estadocivil != 'C' and estadocivil != 'V' and estadocivil != 'D':
    print('Error, tente novamente!')
    print()
    estadocivil = input('Digite seu estado Civil: (S - Solteiro, C - Casado, V - Viúvo e D - Divorciado: )').upper()
print()

print('Tudo no conformes!')