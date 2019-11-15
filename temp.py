with open('input.txt', 'r') as file:
    words = file.readlines()
for word in words:
    word_strip = word.rstrip()
    if word_strip == word_strip[::-1]:
        print(word_strip)