array_a = [5, 0, 4, 2, 3]

# Thuat toan sap xep chen
def InsertionSort(A):
    n = len(A)
    for i in range(1, n):
        value = A[i]
        j = i - 1
        while j >= 0 and A[j] > value:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value

print(array_a)
InsertionSort(array_a)
print(array_a)

print()

array_b = [5, 0, 4, 2, 3]

# Thuat toan sap xep chon
def SelectionSort(A):
    n = len(A)
    for i in range(0, n - 1):
        iMin = i
        for j in range(i, n):
            if A[j] < A[iMin]:
                iMin = j
        A[i], A[iMin] = A[iMin], A[i]

print(array_b)
SelectionSort(array_b)
print(array_b)

print()

array_c = [4, 3, 2, 1]

# Thuat toan sap xep noi bot
def BubbleSort(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            print('j', j)
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            print(A)
        print()

print(array_c)
BubbleSort(array_c)
print(array_c)