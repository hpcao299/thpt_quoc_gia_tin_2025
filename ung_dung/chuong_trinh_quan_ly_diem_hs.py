fname = "Diem.txt"

while(True):
    command = int(input('Nhập điểm của học sinh [1], tra cứu điểm của học sinh [2], thoát chương trình [0]: '))
    if command == 0:
        break
    elif command == 1:
        ten_hs = input('Nhập tên học sinh: ')
        diem_hs = input('Nhập điểm học sinh: ')

        with open(fname, 'a', encoding="UTF-8") as f:
            print(ten_hs, diem_hs, file=f)
    elif command == 2:
        ten_hs_tim_kiem = input('Nhập tên học sinh cần tra cứu điểm: ')
        found_score = ''

        with open(fname, encoding="UTF-8") as f:
            lines = f.readlines()

            for line in lines:
                ten, diem = line.split()
                if ten == ten_hs_tim_kiem:
                    found_score = str(diem)
                    break
        
        if found_score == '':
            print('Không tìm thấy', ten_hs_tim_kiem)
        else:
            print('Tìm thấy ' + ten_hs_tim_kiem + ': ' + str(found_score))



print('Thoát chương trình!')