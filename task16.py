from addInterface import correct_int, creat_int_list

# требуется вычислить, сколько раз встречается некоторое число X в массиве из
# случайных чисел. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

list_1 = creat_int_list(100, 1, 20)
print("Введите число для поиска: ", end="")
num_search = correct_int()
count = 0                       # можно использовать встроенный метод count.
for i in range(len(list_1)):    # он делает то же самое
    if list_1[i] == num_search:
        count += 1
print(*list_1)
if count > 0:
    print(f"Число {num_search} встречается в списке {count} раз.")
else:
    print(f"Числа {num_search} в списке нет.")
