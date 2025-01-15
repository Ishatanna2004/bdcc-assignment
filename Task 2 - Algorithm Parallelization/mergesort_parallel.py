import threading
import cProfile
import random

# Merge Sort Function (Parallelized using threading)
def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = []
    right_sorted = []

    # Create two threads to process the halves in parallel
    left_thread = threading.Thread(target=sort_half, args=(left_half, left_sorted))
    right_thread = threading.Thread(target=sort_half, args=(right_half, right_sorted))

    # Start both threads
    left_thread.start()
    right_thread.start()

    # Wait for both threads to finish
    left_thread.join()
    right_thread.join()

    # Merge the results from both sorted halves
    return merge(left_sorted, right_sorted)


# Helper function for each thread to sort the halves
def sort_half(arr, sorted_half):
    sorted_half[:] = merge_sort_parallel(arr)


# Merge function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(10000)]
    sorted_arr = merge_sort_parallel(arr)
    # Use cProfile with the arr variable directly
    cProfile.run('merge_sort_parallel(arr)')
