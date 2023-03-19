# python3
# Leons Dolgopolovs 221RDB432

def sift_down(arr, i, swaps):
    min = i
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(arr)

    if left < length and arr[left] < arr[min]:
        min = left

    if right < length and arr[right] < arr[min]:
        min = right

    if i != min:
        arr[i], arr[min] = arr[min], arr[i]
        swaps.append((i, min))
        sift_down(arr, min, swaps)

def build_heap(arr):
    swaps = []
    n = len(arr)
    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps)
    return swaps

def main():
    ievade = input()
    if 'F' in ievade:
        path = input()
        path = "tests/" + path
        with open(path, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            
    if 'I' in ievade:
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
