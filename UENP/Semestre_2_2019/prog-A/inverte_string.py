# def invert_string(str_var):
#     return str_var[::-1]

def invert_string(str_var):
    str_invertida = ''.join(reversed(str_var))
    return str_invertida

if __name__ == "__main__":
    string = str(input("Digite uma frase: "))
    print('A string invertida é =', invert_string(string))