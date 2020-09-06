planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

name_file = open('planets.txt', 'w', encoding='utf-8')

# write the names on separate lines
for planet in planets:
    name_file.write(planet + '\n')

name_file.close()