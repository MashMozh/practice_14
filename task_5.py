def get_valid_input() -> list:
    """
    This function accepts user input and checks that
    the entered integers are space-separated.

    Returns:
        list: A list of integers entered by the user.
    """

    while True:
        numbers = input('Введите целые числа через пробел: ').split()

        try:
            return [int(num) for num in numbers]
        except ValueError:
            print('Ошибка: все элементы должны быть целыми числами!')


def average_of_numbers(x: list) -> float:
    """
    The function calculates the average value of numbers in a list.

    Args:
        x (list): A list of integers to process.

    Returns:
        float: The average value of the numbers in the list.
        """
    average = sum(x) / len(x)
    return average


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets valid input from user, calculates average and prints the result.

    Returns:
        None: The function does not return values,
            only prints the result.
    """

    numbers = get_valid_input()
    average = average_of_numbers(numbers)
    print('Среднее значение: ', average)


if __name__ == '__main__':
    main()
