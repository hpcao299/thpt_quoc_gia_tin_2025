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
print('Diem dau tien:', marks[0])
print('Diem cuoi cung:', marks[len(marks) - 1])
print('Diem thap nhat:', Min)
print('Diem cao nhat:', Max)
print()

index = int(input('Tra cuu dau diem thu: '))
while index < 1 or index - 1 > len(marks) - 1:
    print('Dau diem ko hop le, hay nhap lai')
    index = int(input('Tra cuu dau diem thu: '))
print('Dau diem thu ' + str(index) + ': ' + str(marks[index - 1]))