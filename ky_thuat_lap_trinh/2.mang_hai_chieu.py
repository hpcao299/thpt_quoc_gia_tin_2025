DS_diem = [["Quang", 7.5], ["Hà", 8.0], ["Bình", 9.5]]
print(DS_diem)

print("Second data:", DS_diem[1])
print()

print("using for to print data")
for hs,diem in DS_diem:
    print(hs, diem)

print()
print('------------------')
print()

ma_tran = [[12, 10, 91], [11, 45, 20], [15, 34, 55]]

print('using for in to log ma_tran')
for i in ma_tran:
    for j in i:
        print(j, end=" ")
    print()
print()

print('using for range to log ma_tran (3x3)')
for i in range(0, 3):
    for j in range(0, 3):
        print(ma_tran[i][j], end=" ")
    print()
print()