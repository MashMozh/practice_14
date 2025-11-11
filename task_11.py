def shift_elements(numbers: list, quantity: int, direction: str) -> list:
    """
    The function performs a cyclic shift of list elements
    to the right or left.

    Args:
        numbers (list): The list to be shifted.
        quantity (int): The number of positions to shift.
        direction (str): The direction of shift -
                        'R' for right, 'L' for left.

    Returns:
        list: The shifted list.
    """

    if direction == "R":
        first_index = len(numbers) - quantity
        elements = numbers[first_index:]
        numbers[first_index:] = []
        numbers = elements + numbers

    if direction == "L":
        elements = numbers[:quantity]
        numbers[:quantity] = []
        numbers = numbers + elements

    return numbers


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets input from user, processes the shift command
    and displays the result.
    """

    list_1 = input("Введите целые числа через пробел: ").split()

    print("Программа циклически сдвигает элементы. "
          "Общий вид команды: R5. "
          "Буква показывает направление сдвига, "
          "R-вправо, L-влево. "
          "Цифра указывает на сколько позиций "
          "необходимо сдвинуть элементы")

    action = input("Введите команду: ")
    quantity = int(action[1])

    result = shift_elements(list_1, quantity, action[0])
    print(result)


if __name__ == '__main__':
    main()
