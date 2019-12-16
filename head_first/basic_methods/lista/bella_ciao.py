bella_ciao = "Una mattina mi son' svegliato"
letters = list(bella_ciao)

for char in letters[:10]:
    print("\t", char)

for char in letters[12:19]:  # or [-17:-10]
    print("\t"*2, char)

for char in letters[-9:]:
    print("\t"*3, char)