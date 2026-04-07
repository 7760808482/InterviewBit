from collection import orderDict
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    n=int(input())
    item=orderDict()
    for _ in range(n):
        item_id,price=map(int,input().splite())
        if item_id in item:
            item[item_id]+=price
        else:
            item[item_id]=price
    for item_id,total in item.item():
        print(item_id,total)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    return 0

if __name__ == '__main__':
    main()