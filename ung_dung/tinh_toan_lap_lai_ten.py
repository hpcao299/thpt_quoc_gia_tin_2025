names = []

input_names = input('Nhap ten cach nhau boi dau cach: ').strip()
input_names_arr = input_names.split()

# Add base value
names.append([input_names_arr[0], 1])
input_names_arr.pop(0)

for i in range(0, len(input_names_arr)):
    for j in range(0, len(names)):
        if input_names_arr[i] == names[j][0]:
            prev_data = names.pop(j)
            names.append([prev_data[0], prev_data[1] + 1])
            break
        elif j == len(names) - 1:
            names.append([input_names_arr[i], 1])
            break


for i in names:
    print(i[0] + ' -> ' + str(i[1]))