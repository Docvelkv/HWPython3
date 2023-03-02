from addInterface import correct_int, creat_int_list

# требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

list_1 = creat_int_list(10, 0, 100)
print("Введите число для поиска: ", end="")
num_search = correct_int()
dif_num = abs(list_1[0] - num_search)
for i in range(1, len(list_1)):
    if abs(list_1[i] - num_search) < dif_num:
        dif_num = abs(list_1[i] - num_search)
dict_elm = {}
for i in range(len(list_1)):
    if list_1[i] == num_search + dif_num or list_1[i] == num_search - dif_num:
        dict_elm[i + 1] = list_1[i]
print(*list_1)
print(f"Ближайшие элементы: {dict_elm}")  # Вывод можно реализовать по разному
