# python3
#Jēkabs Kindzulis, 221RDC047, 18.gr

def l_child(a):
    return 2 * a + 1

def r_child(a):
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

    if data[l_child(a)] < data[constraint] and l_child(a) < length:
        constraint = l_child(a)

    if data[r_child(a)] < data[constraint] and r_child(a) < length:
        constraint = r_child(a)

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
            f = open("./tests/"+fname, "r")
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            f.close()


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
