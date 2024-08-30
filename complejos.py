def complejo(Num):
    resultado = Num % 4
    if (resultado == 1):
        print('El resultado es: i')
    elif (resultado == 2):
        print('El resultado es: -1')
    elif (resultado == 3):
        print('El resultado es: -i')
    elif (resultado == 0):
        print('El resultado es: 1')
complejo(3)