float_list = list[float]


def map_to_something(multiplier: float, float_numbers_list: float_list) -> float_list:
    mapped_vector = list()
    for i in float_numbers_list:
        mapped_vector.append(i * multiplier)

    return mapped_vector


new_vector = map_to_something(2, [0, 1.1, 2.5])
print(new_vector)
