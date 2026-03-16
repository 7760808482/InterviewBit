'''Given a string S and you have to do certain operations as described in the comments below.'''
def main():
    s = input()
    
    #Print length of the string S
    print(len(s))
    #Print the first occurence of the letter 'a' in S
    print(s.index("a"))
    #Note it is guaranteed that letter a is present in the string S
    print(s[::2])
    #Print all the characters with even index in S
    return 0

if __name__ == '__main__':
    main()