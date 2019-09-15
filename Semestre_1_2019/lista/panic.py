phrase = "Don't panic!"
plist = list(phrase)
plist3 = list(phrase)
print(phrase)
print(plist)
# Challenge: Transform "Don't panic" into "on tap"

# Resolution 1:
for x in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
# --------- #

new_phrase = ''.join(plist) # Transforma em string novamente
print(plist)
print(new_phrase)

# Resolution 2:
remove_letters = ["o", "n", "t", "a", "p", " "]
phrase = phrase.lower()

on_tap = []

for letter in phrase:
    if letter in remove_letters:
        if letter not in on_tap:
            if letter == " ":
                on_tap.insert(2, letter)
            elif letter == "a":
                on_tap.insert(4, letter)
            else:
                on_tap.append(letter)

on_tap = ''.join(on_tap)
print(on_tap)
# --------- #

# Resolution 3:
plist3.remove("'")
plist3.remove(" ")
plist3.insert(3, " ")
plist3.insert(5, "a")
print(''.join(plist3[1:7]))