vowels =['a', 'e', 'i', 'o', 'u']
word = input("Type the sentence to that count the vowels: ")
word = word.lower()

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)

# When needs help:
# >>> help(list)
# >>> help(list.method)