# 05 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

A = int(input('Digite a quantidade da população da cidade A: '))
B = int(input('Digite a quantidade da população da cidade B: '))
taxaA = float(input('Digite a taxa da cidade A: '))
taxaB = float(input('Digite a taxa da cidade B: '))
taxaA = taxaA / 100
taxaB = taxaB / 100
anos = 0

if A <= B or A >= B and taxaA > taxaB:
    if taxaA > taxaB:
        while A <= B:
            A = A + (A * taxaA)
            B = B + (B * taxaB)
            anos = anos + 1
    
    else:
        print()
        print('O valor é invalido!')

    print()
    print ('Serão necessarios {} anos para que a população do país A ultrapasse ou iguale a população do país B'.format(anos))

else:
    print()
    print('O valor é invalido!')