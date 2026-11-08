OPERATORS = ['+', '-', '*', '/', '(', ')']

def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    counts = {op: 0 for op in OPERATORS}
    for ch in expression:
        if ch in counts:
            counts[ch] += 1
    return counts

if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    print(f"Operator counts: {count_operators(expression)}")