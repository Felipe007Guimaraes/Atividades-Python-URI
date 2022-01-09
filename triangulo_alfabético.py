lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def exibe_letras_alfabeto(contador):
    posicao_letra = (lista_alfabeto[contador-1])
    i = 1
    while i <= contador:
        letras_alfabeto = posicao_letra * contador
        i += 1
    print(letras_alfabeto)


entrada = int(input())
if 1 <= entrada <= 26:
    i = 1
    while i <= entrada:
        exibe_letras_alfabeto(i)
        i += 1
       
        
