'''You are given a list of strings, using list comprehensions create a new list of strings called ‘my_list’, which only contain the strings that have odd length'''
def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = [x for x in str_list if len(x) % 2 != 0]
    
    print(my_list)
    return 0

if __name__ == '__main__':
    main()