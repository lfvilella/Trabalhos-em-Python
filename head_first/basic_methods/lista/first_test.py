vowels =['a', 'e', 'i', 'o', 'u']
word = "Exist many vowel in this sentence, look it"
word = word.lower()

for letter in word:
    if letter in vowels:
        print(letter)