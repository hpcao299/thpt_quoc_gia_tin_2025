full_names = ['Tạ Quang Hải', 'Bùi Tiến Phát', 'Vũ Thanh Sơn', 'Nguyễn Văn Hoàn', 'Đặng Quốc Khánh', 'Phan Văn Nam', 'Lê Tuấn Kiệt', 'Đỗ Đức Toàn', 'Hoàng Đức Hoàn', 'Trần Đình Hoàn', 'Phạm Ngọc Hoàn', 'Nguyễn Văn An', 'Dương Chí Nghĩa', 'Tống Trọng Thành', 'Ngô Hoàng Phúc', 'Lê Minh Hoàn', 'Lý Xuân Vinh', 'Trần Quang Huy', 'Hoàng Minh Dũng', 'Phạm Bảo Long']

def LinearSearchName(K):
    found_index = []

    for i in range(len(full_names)):
        full_name = full_names[i]
        full_name_array = full_name.split(' ')
        name = full_name_array[len(full_name_array) - 1]

        if name == K:
            found_index.append(i)
    
    return found_index


found_names_index = LinearSearchName('Phát')

if len(found_names_index) == 0:
    print('Not found any names')
else:
    print('Found:')
    for i in range(len(found_names_index)):
        if i == len(found_names_index) - 1:
            print(full_names[found_names_index[i]])
        else:
            print(full_names[found_names_index[i]], end=", ")
        