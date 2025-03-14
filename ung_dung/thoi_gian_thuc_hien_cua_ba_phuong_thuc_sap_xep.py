from time import perf_counter

array_a = [3, 1, 0, 10, 13, 16, 9, 7, 5, 11]
array_b = [3, 1, 0, 10, 13, 16, 9, 7, 5, 11]
array_c = [3, 1, 0, 10, 13, 16, 9, 7, 5, 11]

def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        k = i - 1

        while k >= 0 and A[k] > value:
            A[k + 1] = A[k]
            k = k - 1
        A[k + 1] = value

def SelectionSort(A):
    n = len(A)
    for i in range(0, n - 1):
        iMin = i
        for j in range(i, n):
            if A[j] < A[iMin]:
                iMin = j
        A[i], A[iMin] = A[iMin], A[i]

def BubbleSort(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
               

t_insertion_1 = perf_counter()
InsertionSort(array_a)
t_insertion_2 = perf_counter()
print(t_insertion_2 - t_insertion_1)

t_selection_1 = perf_counter()
SelectionSort(array_b)
t_selection_2 = perf_counter()
print(t_selection_2 - t_selection_1)

t_bubble_1 = perf_counter()
BubbleSort(array_c)
t_bubble_2 = perf_counter()
print(t_bubble_2 - t_bubble_1)