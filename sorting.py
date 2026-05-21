from random import randint

def bubblesort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def partition(arr: list, lo: int, hi: int) -> int:
    pivot: int = arr[hi]
    idx: int = lo - 1
    for i in range(lo, hi):
        if arr[i] < pivot:
            idx += 1
            arr[idx], arr[i] = arr[i], arr[idx]
    #swap to make sure the pivot is larger than everything already sorted
    idx += 1
    arr[hi], arr[idx] = arr[idx], arr[hi]
    return idx

def quicksort(arr: list, lo: int, hi: int) -> None:
    if lo >= hi:
        return
    pivot_idx = partition(arr, lo, hi)
    quicksort(arr, lo, pivot_idx - 1)
    quicksort(arr, pivot_idx + 1, hi)

def merge(arr1: list, arr2: list) -> list:
    res = []
    i: int = 0 #pointer for arr1
    j: int = 0 #pointer for arr2
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res

def mergesort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    split: int = len(arr) // 2
    arr1 = mergesort(arr[:split])
    arr2 = mergesort(arr[split:])
    return merge(arr1, arr2)

if __name__ == '__main__':
    arr = [randint(0,10) for _ in range(10)]
    mergesort(arr)
    print(arr)
