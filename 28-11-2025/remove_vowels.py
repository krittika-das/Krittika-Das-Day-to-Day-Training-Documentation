def remove_vowels(s):
    k=""
    for i in s:
        if i not in "aeiouAEIOU":
            k=k+i
    return k

print(remove_vowels("Krittika"))