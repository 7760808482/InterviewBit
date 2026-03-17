def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # Change: Use list() instead of tuple() to make them mutable
    list1 = list(tuple1) 
    list2 = list(tuple2)
    
    # Now you can change the values at index 0
    list1[0] = 'number'
    list2[0] = 'number'
    
    # Convert them back to tuples
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()