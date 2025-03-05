arr = [5, 4, 3, 2, 1]
def BinaryReverseSearch(A, K):
    left = 0
    right = len(A) - 1
    step = 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == K:
            print('Buoc ' + str(step) + ' ✅')
            return mid
        elif A[mid] < K:
            right = mid - 1 
            print('Buoc ' + str(step) + ' ❌')
            step = step + 1
        elif A[mid] > K:
            left = mid + 1
            print('Buoc ' + str(step) + ' ❌')
            step = step + 1

print(BinaryReverseSearch(arr, 2))