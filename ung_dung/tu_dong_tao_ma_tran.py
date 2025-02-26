print('Chuong trinh tao ma tran')
number_of_rows = int(input('Nhap so dong muon tao ma tran: '))
number_of_cols = int(input('Nhap so luong so co trong moi dong: '))

matrix = []
for m in range(1, number_of_rows + 1):
    print()
    array = []
    print(f'\033[1;34mDong thu {m}\033[0m')
    for n in range(1, number_of_cols + 1):
        value = int(input(f'Nhap so thu {n}: '))
        array.append(value)
    matrix.append(array)
    
print()
print('\033[1;34mMa tran duoc tao ra\033[0m')
for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
print(matrix)