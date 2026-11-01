def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
    char_count = len(text)
    word_count = len(text.split())
    has_python = "python" in text.lower()
    return char_count, word_count, has_python


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    chars, words, has_python = analyze_sentence(sentence)
    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {has_python}")
