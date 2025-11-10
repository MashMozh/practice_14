def get_valid_input() -> list:
    """
    The function accepts user input and validates that
    exactly 10 integers separated by spaces are entered.

    Returns:
        list: A list of 10 integers entered by the user.
    """

    while True:
        numbers = input('Введите 10 целых чисел через пробел: ').split()

        if len(numbers) != 10:
            print('Ошибка: нужно ввести ровно 10 чисел!')
            continue

        try:
            return [int(num) for num in numbers]
        except ValueError:
            print('Ошибка: все элементы должны быть целыми числами!')


def list_8(x: list) -> list:
    """
    The function creates a new list of 8 elements where each element
    is the sum of adjacent elements from the original list.

    Args:
        x (list): A list of integers to process.

    Returns:
        list: A new list of 8 elements, each being the sum
            of three adjacent elements from the original list.
    """

    new_list = []
    for i in range(1, len(x) - 1):
        j = x[i + 1] + x[i - 1]
        new_list.append(j)
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
    result = list_8(numbers)  # Получаем результат
    print(result)


if __name__ == '__main__':
    main()
