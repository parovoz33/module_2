def calculate_structure_sum(data):
    def recursive_sum(item, total_sum):
        if isinstance(item, int):
            return total_sum + item
        elif isinstance(item, str):
            return total_sum + len(item)
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                total_sum = recursive_sum(element, total_sum)
        elif isinstance(item, dict):
            for key, value in item.items():
                total_sum = recursive_sum(key, total_sum)
                total_sum = recursive_sum(value, total_sum)
        return total_sum

    return recursive_sum(data, 0)

# Пример использования:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)









result = calculate_structure_sum(data_structure)
print(result)

