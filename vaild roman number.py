'''Problem Description

You are given N input string, and you have to validate whether they are valid Roman numeral or not.

If it is valid, print "YES". Otherwise, print "NO". Try to create a regular expression for a valid Roman numeral.

Know more about Roman numeral here

Problem Constraints

1 <= N <= 10

The number will be between 1 and 3999 (both included).

Input Format

First line contains an integer N, the number of inputs.

N lines follow, each containing some string.

Output Format

For every string listed, print "YES" if it is a valid roman numeral and "NO" if it is not on separate lines. Do not print the quotes.

Example Input

3
CDXXI
M
IIX
Example Output

YES
YES
NO'''
import re

def validate_roman():
    # Read number of test cases
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    # The RegEx pattern for 1-3999
    # We use a non-capturing group (optional) and ensure it's not an empty string
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    for _ in range(n):
        s = input().strip()
        
        # Check if match exists and string is not empty
        if s and re.match(pattern, s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    validate_roman()