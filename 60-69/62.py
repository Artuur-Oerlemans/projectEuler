def find_smallest_cube_with_x_anagrams(x):
    number_of_cubes = {}
    index = 1
    while True:
        cube = index ** 3
        cube_id = ''.join(sorted(str(cube)))
        if cube_id not in number_of_cubes:
            number_of_cubes[cube_id] = [cube]
        else:
            number_of_cubes[cube_id].append(cube)
            if len(number_of_cubes[cube_id]) == x:
                return sorted(number_of_cubes[cube_id])[0]
        index += 1


print(find_smallest_cube_with_x_anagrams(5))
