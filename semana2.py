semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
dia = input() 

indice = semana.index(dia)

tempo = int(input()) 

qtd_dias = indice + tempo

if (qtd_dias > 6):
  qtd_dias -= len(semana)

if(semana[qtd_dias] == dia):
  print('chega hoje!')
else:
  print("sera entregue",semana[qtd_dias])