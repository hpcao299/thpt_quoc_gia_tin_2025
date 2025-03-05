A = [1,4,7,8,3,9,10]
B = [1,91,45,23,67,9,10,47,90,46,86]

# Thuat toan tim kiem tuan tu
def LinearSearch(A, K):
    for i in range(len(A)):
        if A[i] == K:
            print('Buoc ' + str(i + 1) + ' ✅')
            return i
        else:
            print('Buoc ' + str(i + 1) + ' ❌')
    return -1

print(LinearSearch(A, 9))
print(LinearSearch(B, 47))

# Thuat toan tim kiem nhi phan
def BinarySearch(A, K):
    A.sort()
    print(A)
    left = 0
    right = len(A) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K:
            print('Buoc ' + str(step) + ' ✅')
            return mid
        elif A[mid] < K:
            left = mid + 1

            print('Buoc ' + str(step) + ' ❌')
            step = step + 1
        elif A[mid] > K:
            right = mid - 1

            print('Buoc ' + str(step) + ' ❌')
            step = step + 1
    return -1

print(BinarySearch(A, 9))