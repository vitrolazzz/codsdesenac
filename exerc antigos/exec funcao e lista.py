def analisar_notas(notas):
    media=sum(notas)/len(notas)
    acima=[]
    for n in notas:
        if n>media:
            acima.append(n)
    aprovados = 0
    for nota in lista_notas:
        if nota >= 7:
            aprovados += 1
    return media, acima, aprovados

lista_notas = [5.5,8,9.5,6,7.5,4]
media, acima, aprovados = analisar_notas (lista_notas)
print (f"Média geral da turma: {media}")
print (f"Notas acima da média: {acima}")
print (f"Alunos aprovados: {aprovados}")
