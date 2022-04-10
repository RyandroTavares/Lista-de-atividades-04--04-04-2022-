# 02 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagemde erro e voltando a pedir as informações.

nome = ' '
senha = 0
while nome != 'ryandro' or senha != 123:
    nome = input('Digite seu nome: ').lower()
    senha = int(input('Digite sua senha: '))
    print('Você digitou o nome {} com a senha {}!'.format(nome, senha))
    print()

print('Seja bem-vindo!')