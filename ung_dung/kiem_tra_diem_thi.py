fname = "Diemthi_sx.txt"

search_score = float(input('Nhập điểm cần tra cứu: '))
score_list = []

f = open(fname)

lines = f.readlines()
for score in lines:
    score_list.append(float(score))

f.close()


start = 0
end = len(score_list) - 1
found_index = -1

while start <= end:
    mid = (start + end) // 2

    if score_list[mid] == search_score:
        found_index = mid
        break
    elif score_list[mid] < search_score:
        start = mid + 1
    elif score_list[mid] > search_score:
        end = mid - 1

if found_index != -1:
    print('Tìm thấy ' + str(search_score) + ' tại dòng ' + str(found_index + 1))
else:
    print('Không tìm thấy ' + str(search_score))