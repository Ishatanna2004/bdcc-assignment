import time
import random

def generate_matrix(size):
    return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

def multiply_matrices(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(size))
    return result

size = 300
A = generate_matrix(size)
B = generate_matrix(size)

iterations = 5
total_time = 0

for _ in range(3):  # Run a few iterations without recording time to warm up JIT compiler for pypy
    result = multiply_matrices(A, B)

for _ in range(iterations):
    start_time = time.time()
    result = multiply_matrices(A, B)
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations

print(average_time)
