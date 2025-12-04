def word_f(sentence):
    words = sentence.lower().split()
    freq={word: words.count(word) for word in words}
    return freq

print(word_f("Hello World is a Hello World"))