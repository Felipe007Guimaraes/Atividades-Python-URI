numero = int(input())
numero >=2
resultado = numero % 2
resultadoImpar1 = numero - 2
resultadoImpar2 = numero + 1
resultadoPar1 = numero - 1
resultadoPar2 = numero + 2
if resultado == 0:
    print(f'{resultadoPar1} {resultadoPar2}')
else:
    print(f'{resultadoImpar1} {resultadoImpar2}')