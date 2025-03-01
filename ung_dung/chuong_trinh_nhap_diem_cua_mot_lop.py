names = []
marks_all = []

number_of_students = int(input('Nhap so hoc sinh co trong lop: '))

for i in range(0, number_of_students):
    print()
    name = input('Nhap ten hoc sinh thu ' + str(i + 1) + ': ')
    names.append(name)

    input_marks = input('Nhap cac diem cua ' + name + ' (cach nhau voi dau cach): ')
    marks = []
    for i in input_marks.split(' '):
        marks.append(float(i))
    marks_all.append(marks)


print()
print('-------------')
print()

max_avg = 0
max_avg_student_name = ''
Min = marks_all[0][0]

print(f'\033[1;34mDiem trung binh cua hoc sinh\033[0m')
for i in range(0, len(names)):
    student_marks = marks_all[i]
    avg_mark = sum(student_marks) / len(student_marks)
    print(names[i] + ' -> ' + str(round(avg_mark, 2)))

    if avg_mark > max_avg:
        max_avg = avg_mark
        max_avg_student_name = names[i]
    for i in student_marks:
        if i < Min:
            Min = i

print('Hoc sinh co diem trung binh cao nhat la ' + max_avg_student_name + ' voi ' + str(round(max_avg, 2)))
print('Con diem thap nhat trong lop:', Min)