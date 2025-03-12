fname = "Data-out.txt"
ten_hs = ['Ha', 'Binh', 'Quang'] 
diem_hs = [9.6, 8.5, 7.2]

f = open(fname, "w", encoding="UTF-8")

for i in range(0, len(ten_hs)):
    print(ten_hs[i], diem_hs[i], file=f)

f.close()
