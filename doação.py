
valor = 0
while True:
    entrada = float(input())
    if entrada == -1.0:
        break
    else:
        valor = valor + entrada
resultado = valor * 2.50
print(f'VC$ {valor:.2f}''\n'f'R${resultado:.2f}')