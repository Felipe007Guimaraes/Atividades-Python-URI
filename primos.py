inicio_sequencia = int(input())
fim_sequencia = int(input())
primos = 0
def primo(valor):
    if valor < 2:
        return False
    elif valor == 2:
        return True 
    else:
        for i in range(2,valor):
            if valor % i == 0:
                return False
        return True

if inicio_sequencia <= fim_sequencia <= 5000:
    while inicio_sequencia <= fim_sequencia:
        if primo(inicio_sequencia) == True:
            print(inicio_sequencia) 
            primos += 1
        inicio_sequencia += 1
    
print(f'primos: {primos}')
