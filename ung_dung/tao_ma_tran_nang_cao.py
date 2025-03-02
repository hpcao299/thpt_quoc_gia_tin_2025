m = int(input('Nhap ma tran co bao gom bao nhieu dong: '))
n = int(input('Nhap ma tran co bao nhieu cot: '))
ma_tran = []

for i in range(0, m):
    print()
    value = input(f'Nhap gia tri cua dong {i + 1}: ')
    value_array = value.split(' ')

    while len(value_array) != n:
        print('Sai so luong cot')
        value = input(f'Nhap gia tri cua dong {i + 1}: ')
        value_array = value.split(' ')

    array = []
    for j in value_array:
        array.append(int(j))
    ma_tran.append(array)

total = 0
max_sum = sum(ma_tran[0])
max_sum_index = []

for i in range(0, len(ma_tran)):
    sum_value = sum(ma_tran[i])
    total = total + sum_value

    if sum_value > max_sum:
        max_sum_index.clear()
        max_sum_index.append(i)
        max_sum = sum_value
    elif sum_value == max_sum:
        max_sum_index.append(i)

ma_tran_count = []
for i in range(0, m):
    for j in range(0, n):
        if ma_tran[i][j] in ma_tran_count:
            continue
        else:
            ma_tran_count.append(ma_tran[i][j])

print()
print('MA TRAN')
for i in range(0, m):
    for j in range(0, n):
        print(ma_tran[i][j], end=" ")
    print()
print()
print('Tong cac phan tu trong ma tran:', total)
for i in max_sum_index:
    print('Dong co tong lon nhat la dong ' + str(i + 1) + ': ' + str(ma_tran[i]))

for i in ma_tran_count:
    print(i, end=" ")
print()

print()
search_value = int(input('Nhap so can tim trong ma tran: '))
search_value_index = []
for i in range(0, m):
    for j in range(0, n):
        if search_value == ma_tran[i][j]:
            search_value_index.append([i, j])
print('So lan xuat hien cua ' + str(search_value) + ': ' + str(len(search_value_index)) + ' tai', end=" ")
for i in search_value_index:
    print(str(i), end=" ")