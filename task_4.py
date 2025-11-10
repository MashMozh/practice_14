def list_of_unique_words(text: list) -> list:
    """
    The function processes a list of words by removing all non-alphabetic characters
    and returns a list of unique words in lowercase.

    Args:
        text (list): A list of words to process.

    Returns:
        list: A new list of unique words containing only alphabetic characters
              in lowercase, without duplicates.
    """

    new_sentence = []
    for word in text:
        for letter in word:
            if not letter.isalpha():
                word = word.replace(letter, '')
        new_sentence.append(word.lower())
        new_sentence = list(set(new_sentence))
    return new_sentence


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets input from user, processes it and prints the result.

    Returns:
        None: The function does not return values,
            only prints the result.
    """

    sentence = input('Введите предложение: ').split()
    result = list_of_unique_words(sentence)
    print(result)


if __name__ == '__main__':
    main()
