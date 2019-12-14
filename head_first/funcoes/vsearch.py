def search_vowels(phrase:str) -> set: # (:str) e (-> set) são apenas notações opcionais
    """ This is a docstring and this is a easy code 
        This function return the vowel in phares """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search_letters(phrase, letters='aeiou'): # Definindo letters caso não tenho arg.
    """ This function return the specific letters in phrase """
    return set(letters).intersection(set(phrase))

if __name__ == "__main__":
    word = input('Type the sentence to that count the vowels: ').lower()
    for vowel in search_vowels(word):
        print(vowel)
    
    letras = input('Type the letters to search on phrase: ').lower()
    for letter in search_letters(word, letras):
        print(letter)

    # Atribuição da palavra-chave:
    print(search_letters(letters='hlo', phrase='The energy of the world is complex'))