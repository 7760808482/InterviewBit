'''You are given three sets X, Y, Z where X contains the children id who loves to play Football, Y contains the children id who loves to play Cricket, and Z contains the children id who loves to play BasketBall. You need to perform operations on these sets as decribed in comments.

Note: You are only required to add your code, no need to change any of the given statements'''
'''
def printset(setx):
    li = list(setx)
    li.sort()
    print(li)
'''
def main():
    # Below are the three sets 
    
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35])
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3])
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14])
    
    # 'set1' contains the student who loves to play all three sports
    set1 = X&Y&Z
    
    print(set(set1))
    
    # 'set2' contains the student who loves to play both Football and Cricket, but don't play Basketball
    set2 = (X&Y)-Z
    
    print(set(set2))
    
    # 'set3' contains the student who loves to play Cricket, but don't loves any other sport
    set3 = Y-(X|Z)
    
    print(set(set3))
    return 0

if __name__ == '__main__':
    main()


'''| Operation                | Math Symbol | Python Symbol | Example      |    |    |
| ------------------------ | ----------- | ------------- | ------------ | -- | -- |
| **Union**                | `∪`         | `             | `            | `A | B` |
| **Intersection**         | `∩`         | `&`           | `A & B`      |    |    |
| **Difference**           | `−`         | `-`           | `A - B`      |    |    |
| **Symmetric Difference** | `⊕`         | `^`           | `A ^ B`      |    |    |
| **Subset**               | `⊆`         | `<=`          | `A <= B`     |    |    |
| **Proper Subset**        | `⊂`         | `<`           | `A < B`      |    |    |
| **Superset**             | `⊇`         | `>=`          | `A >= B`     |    |    |
| **Proper Superset**      | `⊃`         | `>`           | `A > B`      |    |    |
| **Membership**           | `∈`         | `in`          | `x in A`     |    |    |
| **Not in**               | `∉`         | `not in`      | `x not in A` |    |    |'''