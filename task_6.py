def get_single_integer() -> int:
    """
    The function accepts user input and validates that
    exactly one integer is entered.

    Returns:
        int: The integer entered by the user.
    """

    while True:
        user_input = input("Введите одно целое число: ").strip()

        if not user_input:
            print("Ошибка: вы ничего не ввели!")
            continue

        try:
            return int(user_input)
        except ValueError:
            print("Ошибка: введите одно целое число!")


def find_dividers(x: int) -> list:
    """
    The function finds all divisors of a given integer.

    Args:
        x (int): The integer for which to find divisors.

    Returns:
        list: A list of all divisors of the given number,
              or a string message for zero.
    """
    if x == 0:
        return '0 имеет бесконечное число делителей'

    dividers = [1]
    abs_x = abs(x)
    max_divider = abs_x // 2

    for i in range(2, max_divider + 1):
        if abs_x % i == 0:
            dividers.append(i)
    dividers.append(x)

    if x < 0:
        negative_dividers = [-divider for divider in dividers]
        dividers = negative_dividers + dividers


    return dividers


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets a number from user, finds its divisors and prints the result.
    """
    numbers = get_single_integer()
    result = find_dividers(numbers)
    print('Делители числа: ', result)


if __name__ == "__main__":
    main()
