def increase_decrease_distances(distances: list, value: int) -> list:
    """
    The function increases the value of all elements in the sequence which are less or equal to the removed
element with the value of the removed element as well as decreases the value of all elements in the sequence which are greater than the removed element
with the value of the removed element.
    :param distances: The pokemon distance list
    :param value: The index of the caught pokemon
    :return: Updated distance list
    """
    distances = list(map(lambda x: x + value if x <= value else x - value, distances))
    return distances


def check_index_of_distances(index: int) -> int:
    """
    If the given index is less than 0, the function removes the first element of the sequence, and copy the last element
to its place.
If the given index is greater than the last index of the sequence, the function removes the last element from the
sequence, and copies the first element to its place.
The increasing and decreasing elements should also be done in these cases. The element whose value you should
use is the removed element.
    :param index: Index of the element
    :return: The value of the removed element
    """
    if index_of_distances < 0:
        value = pokemon_distances[0]
        pokemon_distances[0] = pokemon_distances[-1]
    elif index_of_distances > len(pokemon_distances) - 1:
        value = pokemon_distances[-1]
        pokemon_distances[-1] = pokemon_distances[0]
    else:
        value = pokemon_distances.pop(index_of_distances)

    return value


pokemon_distances = input().split()
pokemon_distances = list(map(int, pokemon_distances))
sum_of_removed = 0
while len(pokemon_distances) > 0:
    index_of_distances = int(input())
    value_of_removed_element = check_index_of_distances(index_of_distances)
    sum_of_removed += value_of_removed_element
    pokemon_distances = increase_decrease_distances(pokemon_distances, value_of_removed_element)

print(sum_of_removed)
