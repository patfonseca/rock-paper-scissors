word = input()
word_final = ''

for index in range(1, len(word), 2):
    word_final += word[index]

print(word_final)