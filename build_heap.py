# python3

def left_child(a):
    return 2 * a + 1

def right_child(a):
    return 2 * a + 2

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    length = len(data)
    for i in range(length // 2, -1, -1):
        order_heap(i, data, swaps)

    return swaps

def order_heap(a, data, swaps):

    length = len(data)
    constraint = a

    if left_child(a) < length and data[left_child(a)] < data[constraint]:
        constraint = left_child(a)

    if right_child(a) < length and data[right_child(a)] < data[constraint]:
        constraint = right_child(a)

    if a != constraint:
        data[a], data[constraint] = data[constraint], data[a]
        swaps.append((a, constraint))
        order_heap(constraint, data, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard

    temp = input()

    if "I" in temp:
        n = int(input())
        data = list(map(int, input().split()))

    elif "F" in temp:
        fname = input()
        if fname != "a":
            s = open("./tests/"+fname, "r")
            n = int(f.readline())
            data = list(map(int, s.readline().split()))
            s.close()


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
