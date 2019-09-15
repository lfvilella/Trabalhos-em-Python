# def calcula_a_hospedagem(type_of, day):
#     individual = 125
#     suite_dupla = 140
#     suite_tripla = 180
#     total = 0

#     if type_of == "individual":
#         total = individual*day
#     elif type_of == "suíte dupla" or type_of == "suítedupla" or type_of == "suitedupla" or type_of == "suite dupla":
#         total = suite_dupla*day
#     elif type_of == "suíte tripla" or type_of == "suítetripla" or type_of == "suite tripla" or type_of == "suitetripla":
#         total = suite_tripla*day
#     if dia > 2:
#         total = total*0.85
#     return total



# tipo_do_apartamento = str(input()).lower()
# dia = int(input())

# print("%.2f"%calcula_a_hospedagem(tipo_do_apartamento, dia))
import unicodedata

def calcula_a_hospedagem(type_of, day):
    # TIRA OS ESPAÇOS E A ACENTUAÇAO
    type_formatted = (
        unicodedata.normalize('NFKD', (type_of.replace(' ', '').lower()))
        .encode('ascii', 'ignore')
    )

    # print(type_formatted)

    individual = 125
    suite_dupla = 140
    suite_tripla = 180
    total = 0

    if type_formatted == b"individual":
        total = individual*day
    elif type_formatted == b"suitedupla":
        total = suite_dupla*day
    elif type_formatted == b"suitetripla":
        total = suite_tripla*day
    if dia > 2:
        total = total*0.85
    return total

tipo_do_apartamento = input()
dia = int(input())

print("%.2f"%calcula_a_hospedagem(tipo_do_apartamento, dia))

