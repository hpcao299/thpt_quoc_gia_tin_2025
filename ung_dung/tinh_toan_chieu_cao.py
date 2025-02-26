# 30 students
students = [
    ["Max", 150], ["Alice", 160], ["Bob", 155], ["Charlie", 170], ["David", 165],
    ["Emma", 180], ["Frank", 175], ["Grace", 168], ["Henry", 172], ["Isabella", 158],
    ["Jack", 162], ["Kate", 177], ["Leo", 169], ["Mia", 185], ["Noah", 174],
    ["Olivia", 159], ["Paul", 171], ["Quinn", 181], ["Ryan", 178], ["Sophia", 166],
    ["Tom", 163], ["Uma", 167], ["Victor", 182], ["Wendy", 176], ["Xander", 157],
    ["Yara", 173], ["Zack", 164], ["Ethan", 179], ["Lily", 183], ["Daniel", 161]
]
height = []
student_above_average_height_count = 0;

for i in students:
    height.append(i[1])

print('Average height:', sum(height) // len(students), 'cm')

for i in students:
    if i[1] > sum(height) // len(students):
        student_above_average_height_count = student_above_average_height_count + 1

print('Number of students above average height:', student_above_average_height_count)

print()
print('------------------')
print()

while True:
    name = input("Type name to search student's height [e: exit]: ")
    if name == 'e':
        break;
    
    found_student = []
    for i in students:
        if i[0] == name:
            found_student = i
            break
    
    if len(found_student) == 0:
        print('Not found any student with name:', name)
    else:
        print('Found', found_student[0], 'with height:', found_student[1])
    print()

print('Exited.')
    