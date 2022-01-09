lista_de_dias = ['domingo' , 'segunda' , 'terca' , 'quarta' , 'quinta' , 'sexta' , 'sabado']
valor_digitado = input()
quantidade_de_dias = int(input())
tamanho_da_lista = len(lista_de_dias)
indice_do_dia_da_semana = lista_de_dias.index(valor_digitado)
nova_lista = lista_de_dias[indice_do_dia_da_semana+1: tamanho_da_lista]
nova_lista = nova_lista + lista_de_dias[0:indice_do_dia_da_semana]
dia_da_entrega = nova_lista[quantidade_de_dias-1]
if quantidade_de_dias == 0:
        print('chega hoje!')
else:
        print('será entregue',dia_da_entrega)