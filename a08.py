def vowel_word(word):
    list = ['a', 'e','i','o','u']
    for letter in word:
        if letter in list:
            list.remove(letter)
    if len(list) == 0:
        return True
    else:
        return False

print(vowel_word('facetious'))