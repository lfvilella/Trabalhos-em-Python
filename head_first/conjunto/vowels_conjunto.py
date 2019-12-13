vowels = set('aeiou')
word = input("Type the sentence to that count the vowels: ").lower()

found = vowels.intersection(set(word))

for vowel in sorted(found):
    print(vowel)