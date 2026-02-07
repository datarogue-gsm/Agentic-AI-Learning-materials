def get_number(prompt):
    """Prompt the user for a number until valid input is provided."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")