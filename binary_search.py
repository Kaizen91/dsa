from random import randint

def binary_search(arr: list[int], needle: int) -> tuple[bool, int]:
    hi: int = len(arr)
    low: int = 0
    while low < hi:
        mid: int = low + (hi - low) // 2
        if arr[mid] == needle:
            return True, mid
        elif needle < mid:
            hi = mid
        else:
            low = mid + 1
    return False, -1


if __name__ == '__main__':
    arr = [randint(1,100) for _ in range(100)] 
    arr.sort()
    print(arr)
    res, index = binary_search(arr, 15)
    if res:
        print(f'found at {index}')
    else:
        print('not found')
