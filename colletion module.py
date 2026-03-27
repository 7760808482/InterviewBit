'''You are given two list of lowercase characters A of length N and B of length M. For each ith character in B print space separated indices of all the occurence of B[i] in A in a new line.

If the character is not present in A, then print -1.
 Considered index to be 0-based.

Example Input

A = ['a', 'a', 'b', 'a', 'b', 'c', 'x']
B = ['a', 'x', 'z']
Example Output

0 1 3 
6 
-1 '''

def main():
    A = input().split()
    B = input().split()
    
    for i in B:
        found = False
        
        for index in range(len(A)):
            if A[index] == i:
                print(index, end=" ")
                found = True
        
        if not found:
            print(-1, end="")
        
        print()   # new line

if __name__ == '__main__':
    main()