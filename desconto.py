
valor_mercadoria = float(input())
quantidade = int(input())
valor_total = quantidade * valor_mercadoria
desconto_fixo =   0.1
desconto_unidade = quantidade * 0.01
desconto_total = valor_total *(desconto_fixo + desconto_unidade)
preco_total_final = valor_total - desconto_total
print(f'{valor_total:.2f}')
print(f'{preco_total_final:.2f}')