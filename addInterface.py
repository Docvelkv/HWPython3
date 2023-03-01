from random import randint as irand, random as frand


def correct_int() -> int:
    """Ввод целого числа с обработкой некорректного введения"""
    is_correct = True
    while is_correct:
        num_int = input()
        try:
            num_int = int(num_int)
            is_correct = False
            return num_int
        except ValueError:
            print("Это не целое число. Введите снова:")


def creat_int_list(num_elm: int, min_val: int, max_val: int):
    """Создание списка из целых чисел"""
    list_1 = [irand(min_val, max_val) for i in range(num_elm)]
    return list_1


def creat_float_list(num_elm: int, min_val: int, max_val: int, ndig: int):
    """Создание списка из вещественных чисел"""
    list_1 = [irand(min_val, max_val) + round(frand(), ndig)
              for i in range(num_elm)]
    return list_1
