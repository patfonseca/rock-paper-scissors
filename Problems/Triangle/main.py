triangle_height = int(input())
triangle = '#'

for _ in range(triangle_height):
    print(triangle.center(2 * triangle_height))
    triangle = '#' + triangle + '#'