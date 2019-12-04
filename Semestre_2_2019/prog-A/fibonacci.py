def fibonacci(numero):
     if numero <= 1:
        return numero
     else:
        return fibonacci(numero-1) + fibonacci(numero-2)

if __name__ == "__main__":
    num = int(input("Digite um numero: "))
    print("A sequencia de Fibonacci =", fibonacci(num))