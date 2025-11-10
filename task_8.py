def sorted_string(sentence: str) -> str:
    """
    The function takes a string, converts it to a list of characters,
    sorts the list, converts it back to a string and returns the result.

    Args:
        sentence (str): The input string to be sorted.

    Returns:
        str: The sorted string with characters in alphabetical order.
    """

    symbols = []
    for symbol in sentence:
        symbols.append(symbol)
    symbols.sort()
    result = ''.join(symbols)
    return result


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets input from user, processes it and prints the sorted string.
    """

    text = input("Введите строку: ")
    sorted_text = sorted_string(text)
    print("Отсортированная строка: ", sorted_text)


if __name__ == '__main__':
    main()
