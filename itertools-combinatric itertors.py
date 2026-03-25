'''You are given a string S containing distinct characters.

Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Constraints

1 <= K <= len(S)
String S consist of lowercase letters.
Input Format

First line contains space separated input S and K.
Output Format

Print the permutations of the string S of size K on separate lines.
Example Input

one 2
Example Output

eo
en
ne
no
oe
on'''

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    from itertools import permutations
    s,k=input().splite()
    k=int(k)
    s=sorted(s)
    for p in permutations(s,k):
        print("",join(p))
    
    return 0

if __name__ == '__main__':
    main()