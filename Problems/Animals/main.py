file = open('animals.txt', 'r')
new_file = open('animals_new.txt', 'w', encoding='utf-8')
list_animals = []

for line in file:
    list_animals.append(line)

for word in list_animals:
    word = word.rstrip('\n')
    new_file.write(word + ' ')

file.close()
new_file.close()

