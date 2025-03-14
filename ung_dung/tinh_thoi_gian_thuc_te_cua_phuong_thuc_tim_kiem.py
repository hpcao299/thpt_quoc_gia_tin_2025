from time import perf_counter

def BinarySearch(A, K):
    n = len(A)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == K:
            return mid;
        elif A[mid] < K:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def LinearSearch(A, K):
    for i in range(0, len(A)):
        if A[i] == K:
            return i
    return -1

array_a = [3, 1, 0, 10, 13, 9, 16, 7, 5, 11]
sorted_array_a = [0, 1, 3, 5, 7, 9, 10, 11, 13, 16]

t1 = perf_counter()
result1 = LinearSearch(array_a, 9)
t2 = perf_counter()

t3 = perf_counter()
result2 = BinarySearch(sorted_array_a, 9)
t4 = perf_counter()

print('LinearSearch:', result1)
print('BinarySearch:', result2)
if t2 - t1 > t4 - t3:
    print('LinearSearch chậm hơn BinarySearch')
else:
    print('BinarySearch chậm hơn LinearSearch')
