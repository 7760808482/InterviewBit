'''Exaple Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '#'
2'''
import sys

def main():
    # Read the number of test cases
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        t = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        # Read the pair of values
        input_data = sys.stdin.readline().split()
        
        try:
            # Attempt to convert and divide
            a = int(input_data[0])
            b = int(input_data[1])
            print(a // b)
            
        except ZeroDivisionError as e:
            # Catch division by zero
            print("Error Code:", e)
            
        except ValueError as e:
            # Catch invalid literal for int()
            print("Error Code:", e)
        
        except IndexError:
            # Handle cases where input might be missing a value
            continue

if __name__ == '__main__':
    main()