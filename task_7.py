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


def even_or_odd(x: list) -> tuple:
    """
    The function calculates the sum of even and odd numbers in a list.

    Args:
        x (list): A list of integers to process.

    Returns:
        tuple: A tuple containing (sum_of_evens, sum_of_odds)
    """
    new_numbers = []
    even_numbers = []
    odd_numbers = []

    for number in x:
        number = int(number)
        new_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return sum(even_numbers), sum(odd_numbers)


def main() -> None:
    """
    The main function that coordinates the program execution.
    """

    numbers = get_valid_input()
    even_sum, odd_sum = even_or_odd(numbers)

    print('Сумма четных элементов: ', even_sum)
    print('Сумма нечетных элементов: ', odd_sum)


if __name__ == '__main__':
    main()
