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
