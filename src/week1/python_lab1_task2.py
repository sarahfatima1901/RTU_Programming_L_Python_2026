def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    cleaned = name.strip()
    if not cleaned:
        cleaned = "Stranger"
    return f"Hello, {cleaned.capitalize()}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
