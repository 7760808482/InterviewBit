import itertools
import operator

def main():
    arr1 = [2, 1, 3, 4, 1]
    arr2 = [1, 2, 4]
    arr3 = [10, 3, 4, 3, 5, 6, 32, 11]
    
    # join all arrays using chain()
    arr4 = list(itertools.chain(arr1, arr2, arr3))
    
    print(arr4)
    
    # successive multiplication using accumulate()
    arr5 = list(itertools.accumulate(arr4, operator.mul))
    
    print(arr5)
    
    return 0

if __name__ == '__main__':
    main()