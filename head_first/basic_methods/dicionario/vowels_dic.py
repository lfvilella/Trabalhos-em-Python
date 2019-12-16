vowels = ('a', 'e', 'i', 'o', 'u') # Tuple
word = input("Type the sentence to that count the vowels: ").lower()

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) # It's similar to if/not in
        # if letter not in found:
        #     found[letter] = 0
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s)')