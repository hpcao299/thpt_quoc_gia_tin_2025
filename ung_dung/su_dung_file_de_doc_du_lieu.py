fname = "Data.txt"

ten_hs = []
diem_hs = []

f = open(fname, 'r', encoding="UTF-8")

lines = list(f.readlines())

for line in lines:
    splitted_line = line.split(' ')

    ten_hs.append(str(splitted_line[0]))
    diem_hs.append(float(splitted_line[1]))

f.close()

for i in range(0, len(ten_hs)):
    print(ten_hs[i] + ' ' + str(diem_hs[i]))