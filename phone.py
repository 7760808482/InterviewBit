import re

def validate_mobile_numbers():
    # Read the number of inputs
    try:
        n = int(input().strip())
    except EOFError:
        return

    # Define the regex pattern
    # [6-9] is shorthand for [6789]
    pattern = r"^[6-9]\d{9}$"

    for _ in range(n):
        s = input().strip()
        # re.match checks if the pattern matches the string from the beginning
        # Since we use ^ and $, it ensures the entire string matches exactly
        if re.match(pattern, s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    validate_mobile_numbers()