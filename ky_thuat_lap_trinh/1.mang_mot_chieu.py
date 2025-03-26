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

# Slice
a = [1,3,5,7,9,11]
b = a[2:1]

# Bộ nhớ
c = [1, 3, 2, 5]
d = c
print(d, c)
c.append(4)
print(d,c)
d.sort()
print(d,c)
c = [1, 3]
print(d,c)
d.clear()
print(d,c)
c = d
c.append(1)
print(d,c)
d = c[:]
d.append(1)
print(d,c)

print()
# Sorted
array_unsort = [6, 2.3, 4, 9, 10, 2, 3]
abc = sorted(array_unsort)

print(abc)
print(array_unsort)
abc[0] = 1
print(abc)
print(array_unsort)
print(array_unsort.sort())
print(array_unsort)