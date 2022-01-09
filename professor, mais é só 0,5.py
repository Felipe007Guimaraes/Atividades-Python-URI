notaTrabalho = float(input())
notaProva = float(input())
media = float(notaTrabalho + notaProva)/2
if notaTrabalho < 2:
    print('reprovado')
elif media < 6:
    print('talvez com a sub')
elif media >= 6:
        print('aprovado')
else:
    print('aprovado')