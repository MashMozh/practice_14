def get_valid_input() -> list:
    """
    The function accepts user input and validates that
    exactly 10 integers separated by spaces are entered.

    Returns:
        list: A list of 10 integers entered by the user.
    """

    while True:
        numbers = input('Введите 10 целых чисел через пробел: ').split()

        if not numbers:
            print('Ошибка: вы ничего не ввели!')
            continue

        try:
            return [int(num) for num in numbers]
        except ValueError:
            print('Ошибка: все элементы должны быть целыми числами!')


def even_or_odd(x: list) -> tuple:
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
    print('Сумма нечетных элементов: ',  odd_sum)


if __name__ == '__main__':
    main()
