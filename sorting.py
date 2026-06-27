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

def merge(arr: list[int], lo: int, mid: int, hi: int) -> None:
    L: list[int] = arr[lo:mid]
    R: list[int] = arr[mid:hi]
    L.append(float('inf'))
    R.append(float('inf'))
    i: int
    j: int
    i = j = 0
    for k in range(lo, hi):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def mergesort(arr: list) -> None:
    hi: int = len(arr)
    lo: int = 0
    mergesort_recursive(arr, lo, hi)
    
def mergesort_recursive(arr, lo: int, hi: int) -> None:
    if hi - lo > 1:
        mid: int = (hi + lo) // 2
        mergesort_recursive(arr, lo, mid)
        mergesort_recursive(arr, mid, hi)
        merge(arr, lo, mid, hi)


if __name__ == '__main__':
    arr = [randint(0,10) for _ in range(10)]
    mergesort(arr)
    print(arr)
