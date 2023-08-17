from dataclasses import dataclass
from operator import attrgetter

@dataclass(order=True)
class Person:
    """A simple data class representing a person with a name and surname."""
    name: str
    surname: str

def find_index(elements, value, key):
    """
    Find the index of a specific value within a sorted list using binary search.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        int: Index of the found value, or None if not found.
    """
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

def contains(elements, value, key=lambda x: x):
    """
    Check if a value exists in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        bool: True if the value exists, False otherwise.
    """
    return find_index(elements, value, key) is not None

def find(elements, value, key=lambda x: x):
    """
    Find a single element in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        Any: The found element, or None if not found.
    """
    index = find_index(elements, value, key)
    return None if index is None else elements[index]

def find_leftmost_index(elements, value, key=lambda x: x):
    """
    Find the index of the leftmost occurrence of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        int: Index of the leftmost occurrence, or -1 if not found.
    """
    index = find_index(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1
    return index

def find_rightmost_index(elements, value, key=lambda x: x):
    """
    Find the index of the rightmost occurrence of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        int: Index of the rightmost occurrence, or -1 if not found.
    """
    index = find_index(elements, value, key)
    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        index -= 1
    return index

def find_all_indices(elements, value, key=lambda x: x):
    """
    Find all indices of occurrences of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        set: A set of indices where the value is found.
    """
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left <= right:
        return set(range(left, right + 1))
    return set()

def find_leftmost(elements, value, key=lambda x: x):
    """
    Find the leftmost occurrence of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        Any: The leftmost element, or None if not found.
    """
    index = find_leftmost_index(elements, value, key)
    return None if index is None else elements[index]

def find_rightmost(elements, value, key=lambda x: x):
    """
    Find the rightmost occurrence of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        Any: The rightmost element, or None if not found.
    """
    index = find_rightmost_index(elements, value, key)
    return None if index is None else elements[index]

def find_all(elements, value, key=lambda x: x):
    """
    Find all occurrences of a value in the sorted list.

    Args:
        elements (list): The sorted list of elements.
        value: The value to search for.
        key (function): A function to extract a comparable key from elements.

    Returns:
        list: A list of all elements with the specified value.
    """
    return [elements[i] for i in find_all_indices(elements, value, key)]

people = [
    Person('Bob', 'Williams'),
    Person('John', 'Doe'),
    Person('Paul', 'Brown'),
    Person('Alice', 'Smith'),
    Person('John', 'Smith'),
]

by_surname = attrgetter('surname')
people.sort(key=by_surname)

# Find all people with the surname 'Smith' and print the result.
print(find_all(people, key=by_surname, value='Smith'))