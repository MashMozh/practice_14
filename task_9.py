from collections import Counter


def text_input() -> list:
    """
    The function accepts text input from the user until an empty line is entered.

    Returns:
        list: A list of strings representing the input text lines.
    """

    print("Введите текст. Чтобы завершить ввод нажмите 2 раза Enter")
    lines = []

    while True:
        line = input()
        if line == '':
            break
        lines.append(line)

    return lines


def sorted_words(text: list) -> None:
    """
    The function processes text lines, cleans words from punctuation,
    counts word frequencies and prints words sorted by frequency 
    and appearance order.

    Args:
        text (list): A list of text lines to process.
    """

    words = []

    for ln in text:
        line_words = ln.split()
        for word in line_words:
            for letter in word:
                if not letter.isalpha():
                    word = word.replace(letter, '')
            words.append(word)

    word_counts = Counter(words)
    sorted_word = []

    for word, count in word_counts.most_common():
        sorted_word.append(word.lower())

    print('\n'.join(sorted_word))


def main() -> None:
    """
    The main function that coordinates the program execution:
    gets text input, processes it and prints sorted words.
    """

    sentences = text_input()
    sorted_words(sentences)


if __name__ == '__main__':
    main()
