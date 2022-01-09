"""
Pague o aluguel!!!
 Para quitar a dívida, prometendo pagar mensalmente um valor que será descontado da dívida total.
  Ele se comprometeu a sempre pagar o mesmo valor até que a dívida seja encerrada. Porém, se o valor
   que ele puder pagar superar o valor da dívida, ele pagará exatamente o que deve e não mais, evidentemente.
 pediu sua ajuda para construir um programa que receba como entrada o valor da dívida e
  o valor que se comprometeu a pagar mensalmente, o programa deve exibir, mês a mês, o valor da dívida 
  antes e depois do pagamento.
Entrada
Dois números inteiros positivos, o primeiro representa o valor total da dívida e o segundo o valor 
a ser pago mensalmente.
Saída
O número do pagamento, o valor restante da dívida antes do pagamento mensal e o valor restante da dívida após 
o pagamento mensal, conforme o padrão exibido nos exemplos. 
A exibição deve continuar até que a dívida seja quitada.

"""
valor_da_divida = int(input())
valor_a_ser_pago = int(input())
antes = valor_da_divida
pagamentos = 0

while valor_da_divida > 0:
    if valor_a_ser_pago <= valor_da_divida:
        valor_da_divida = valor_da_divida - valor_a_ser_pago
        fim = valor_da_divida
    elif valor_da_divida <= valor_a_ser_pago:
        fim = 0
        pagamentos += 1
        print (f'pagamentos: {pagamentos}')
        print(f'antes = {antes}')
        print(f'depois = {fim}')
        print( f'-----' )
        break
    pagamentos += 1
    print (f'pagamentos: {pagamentos}')
    print(f'antes = {antes}')
    print(f'depois = {fim}')
    print( f'-----' )



