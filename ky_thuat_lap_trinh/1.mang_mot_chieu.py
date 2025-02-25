A = [1,3,5,7,9,11]

print(A)
print()

print("append 13 to A")

A.append(13)

print(A)
print()

print("remove 9 out of A")

A.remove(9)

print(A)
print()

print("insert 9 back to A")

A.insert(4, 9)

print(A)
print()

print("sum A:",sum(A))
print()

print('using for range to log out all array items')

for i in range(0, len(A), 1):
    print(A[i], end=" ")
print()
print()

print('using for in to log out all array items')
for i in A:
    print(i, end=" ")
print()
print()

print('using for to print backward')
for i in range(len(A) - 1, -1, -1):
    print(A[i], end=" ")
print()
print()

print("clear A")

A.clear()

print(A)
print()