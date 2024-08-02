def count_occurrences(lst, element):
    return lst.count(element)
# Example usage
numbers = [1, 2, 3, 4, 2, 5, 2, 6, 2, 7]
element_to_count = 2
count = count_occurrences(numbers, element_to_count)
print(f"Element {element_to_count} occurs {count} times in the list.")
"""Output:
Element 2 occurs 4 times in the list.
"""
