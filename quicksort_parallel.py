from multiprocessing import Pool

def parallel_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with Pool() as pool:
        left, right = pool.map(parallel_quicksort, [left, right])
    return left + middle + right
