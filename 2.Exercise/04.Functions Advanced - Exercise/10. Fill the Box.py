def fill_the_box(height, length, width, *cubes):
    box_volume = height * length * width
    total_cubes_volume = sum(cube for cube in cubes if isinstance(cube, int))
    if "Finish" in cubes:
        return f"There is free space in the box. You could put {box_volume - total_cubes_volume} more cubes."
    elif total_cubes_volume > box_volume:
        return f"No more free space! You have {total_cubes_volume - box_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
