# python3
def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    length = len(data)
    for i in range(length // 2, -1, -1):
        order_heap(data, i, swaps)

    return swaps

def order_heap(data, i, swaps):

    max_index = i
    left = left_child(i)
    if left < len(data) and data[left] < data[max_index]:
        max_index = left
    right = right_child(i)
    if right < len(data) and data[right] < data[max_index]:
        max_index = right
    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(data, max_index, swaps)

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
