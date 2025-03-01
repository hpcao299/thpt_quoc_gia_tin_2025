marks = []
input_marks = input('Nhap diem cac mon cach nhau bang dau cach: ')

for x in input_marks.split():
    marks.append(float(x))

Min = marks[0]
Max = marks[0]

for i in marks:
    if (i < Min):
        Min = i
    if (i > Max):
        Max = i
    
print()
print('Diem trung binh:', sum(marks) / len(marks))
print('Diem thap nhat:', Min)
print('Diem cao nhat:', Max)