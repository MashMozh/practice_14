def hole_or_not(words: list[str]) -> tuple[int, int]:
    """
    Counts the number of letters with and without holes
    in a list of words.

    Args:
        words (list[str]): List of lowercase words.

    Returns:
        tuple[int, int]: A tuple containing two numbers:
            - count of letters with holes
            - count of letters without holes
    """

    holes = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    letters_with_hole = 0
    letters_without_hole = 0

    for word in words:
        for letter in word:
            if letter in holes:
                letters_with_hole += 1
            else:
                letters_without_hole += 1

    return letters_with_hole, letters_without_hole


def words_two_holes(words: list[str]) -> list[str]:
    """
    Creates a list of words that contain two or more
    letters with holes.

    Args:
        words (list[str]): List of lowercase words.

    Returns:
        list[str]: List of words that have at least
        two letters with holes.
    """

    holes = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    result = []

    for word in words:
        count = sum(1 for letter in word if letter in holes)
        if count >= 2:
            result.append(word)

    return result


def main() -> None:
    """
    The main function that handles user input,
    processes data, and prints results.
    """

    text = input("Enter lowercase words separated by spaces: ")
    words = text.split()

    holes_count, no_holes_count = hole_or_not(words)
    words_with_two_holes = words_two_holes(words)

    print("Number of letters with holes:", holes_count)
    print("Number of letters without holes:", no_holes_count)
    print("Words with two or more holes:", words_with_two_holes)


if __name__ == '__main__':
    main()
