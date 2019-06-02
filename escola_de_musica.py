# class = maiusculo
# def = minusculo
def classifica_aluno(note, faults):
    if faultas > 10:
        resultado = "REPROVADO POR FALTAS"
    else:
        if note < 7:
            resultado = "REPROVADO"
        else:
            if note < 9.5:
                resultado = "APROVADO"
            else:
                resultado = "APROVADO COM LOUVOR"
    
    return resultado

nota = float(input())
faultas = int(input())

print(classifica_aluno(nota, faultas))