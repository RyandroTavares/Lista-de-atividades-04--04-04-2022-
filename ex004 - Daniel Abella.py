# 04 Supondo que a população de um país 'A' seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3%
# e que a populaçãode 'B' seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país 'A' ultrapasse ou iguale a população do país 'B', mantidas as taxas de crescimento.

A = 80000 
B = 200000
taxaA = 0.03
taxaB = 0.015

anos = 0
while A <= B:
    A = A + (A * taxaA)
    B = B + (B * taxaB)
    anos = anos + 1
    
print()
print ('Serão necessarios {} anos para que a população do país A ultrapasse ou iguale a população do país B'.format(anos))