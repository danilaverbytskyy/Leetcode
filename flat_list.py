nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_list = [i for elem in nested_list for i in elem]
print(flat_list)  # Вывод: [1, 2, 3, 4, 5, 6, 7, 8, 9]