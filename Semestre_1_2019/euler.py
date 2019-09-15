print("Bem vindo a Calculadora de Periodo (n) !")
print("Insira o periodo: ")

# Le o valor na Variavel
n  = int(input())

somatorio = 0

# Calcula o valor de euler com o valor de "n"
for i in range(n+1):
    
    # O fatorial de um numero elevado a 0 é 1
    if(i == 0):
        fatorial = 1
        
    else:
        for j in range(1, i+1):
            fatorial *= float(j)

            # print(1/fatorial) -> Caso queira ver melhor em execuçao


    # Divide por 1, para chegar ao numero de euler     
    somatorio += (1/fatorial)
    
    fatorial = 1
    #reinicia-se o valor da variável fatorial
    
print("O resultado é:", somatorio)
