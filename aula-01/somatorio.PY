def soma(N1,N2):
    resultado = N1 + N2 
    return resultado
def principal():
    numero1 = int(input('Digite o 1°número'))
    numero2 = int(input('Digite o 2° número'))
    somatorio = soma(numero1,numero2)
    print('O somatório é:', somatorio)
principal()