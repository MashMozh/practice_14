def get_valid_input() -> list:
    """
    The function accepts user input and validates that
    exactly 10 integers separated by spaces are entered.

    Returns:
        list: A list of 10 integers entered by the user.
    """

    while True:
        numbers = input('Введите 10 целых чисел через пробел: ').split()

        try:
            return [int(num) for num in numbers]
        except ValueError:
            print('Ошибка: все элементы должны быть целыми числами!')


def list_without_3(x: list) -> list:
    """
    The function creates a new list by removing all occurrences of number 3.

    Args:
        x (list): A list of integers to process.

    Returns:
        list: A new list without number 3.
    """

    new_list = []
    for number in x:
        if number != 3:
            new_list.append(number)
    return new_list


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets valid input from user, processes it and prints the result.

    Returns:
        None: The function does not return values,
            only prints the result.
    """

    numbers = get_valid_input()
    result = list_without_3(numbers)
    print(result)


if __name__ == '__main__':
    main()
