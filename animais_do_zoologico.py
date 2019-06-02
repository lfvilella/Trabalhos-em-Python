import unicodedata

many_monkeys = 0
tigers_middleweight = 0
many_tigers = 0
sum_weight_tigers = 0
many_snakes = 0
prossegue = True
while prossegue == True:
    type_of_animal = str(input())
    weight = float(input())
    source = str(input())
    comando_de_continuacao = str(input())

    # TIRA OS ESPA�OS E A ACENTUA�AO
    type_formatted_animal = (
        unicodedata.normalize('NFKD', (type_of_animal.replace(' ', '').lower()))
        .encode('ascii', 'ignore')
    )
    source_formatted = (
        unicodedata.normalize('NFKD', (source.replace(' ', '').lower()))
        .encode('ascii', 'ignore')
    )
    command_formatted = (
        unicodedata.normalize('NFKD', (comando_de_continuacao.replace(' ', '').lower()))
        .encode('ascii', 'ignore')
    )
    
    # print(type_formatted_animal)
    # print(source_formatted)
    # print(command_formatted)

    if command_formatted == b"parar":
        prossegue = False
    elif command_formatted == b"continuar":
        prossegue = True

    if type_formatted_animal == b"macaco":
        many_monkeys += 1

    elif type_formatted_animal == b"tigre":
        many_tigers += 1
        sum_weight_tigers += weight
        tigers_middleweight = sum_weight_tigers/many_tigers

    elif type_formatted_animal == b"cobra":
        if source_formatted == b"venezuela":
            many_snakes += 1

print(many_monkeys)
print("%.2f"%tigers_middleweight)
print(many_snakes)