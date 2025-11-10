def get_lists_from_input() -> tuple:
    """
    The function reads two lists of integers from user input.

    Returns:
        tuple: A tuple containing two lists (list1, list2)
    """

    list_1 = input("Введите целые числа для первого списка через пробел: ").split()
    list_2 = input("Введите целые числа для второго списка через пробел: ").split()

    return list_1, list_2


def new_lists(list_1: list, list_2: list, first_num: int, last_num: int) -> tuple:
    """
    The function transfers elements from list_1 to list_2 in reverse order
    and removes them from list_1.

    Args:
        list_1 (list): The source list to transfer elements from
        list_2 (list): The target list to transfer elements to
        first_num (int): First element index of the range (1-based)
        last_num (int): Last element index of the range (1-based)

    Returns:
        tuple: A tuple containing modified (list_1, list_2)
    """

    new_elements = list_1[first_num - 1:last_num]
    list_1[first_num - 1:last_num] = []
    list_2 = list_2 + new_elements[::-1]

    return list_1, list_2


def main():
    """
        The main function that coordinates the program execution.
    """

    first_number = int(input("Введите номер первого элемента диапазона: "))
    last_number = int(input("Введите номер последнего элемента диапазона: "))

    list_1, list_2 = get_lists_from_input()
    result_list_1, result_list_2 = new_lists(list_1, list_2, first_number, last_number)

    print("Первый список после преобразований:", result_list_1)
    print("Второй список после преобразований:", result_list_2)


if __name__ == '__main__':
    main()


