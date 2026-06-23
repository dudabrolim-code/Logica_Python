def quadrado(n1):
    resultado = n1**2
    return resultado

def principal():
    numero1 = int(input('Digite n1:'))

    resultado = quadrado(numero1)
    print('O quadrado é:',resultado)
principal()