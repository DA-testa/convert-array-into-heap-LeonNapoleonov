# python3
# Leons Dolgopolovs 221RDB432

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1, -1):
        swaps += heapify(data, n, i)
    return swaps

def heapify(data, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and data[left] < data[largest]:
        largest = left
    if right < n and data[right] < data[largest]:
        largest = right
    if i != largest:
        data[i], data[largest] = data[largest], data[i]
        swaps = [(i, largest)]
        swaps += heapify(data, n, largest)
        return swaps
    return []

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

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
