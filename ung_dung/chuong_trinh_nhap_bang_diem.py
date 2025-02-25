print('-------------------------')

command = input('Do you want to run program managing students score [0: yes]: ')
if command == "0":
    bang_diem = []
    while True:
        print()
        name = input("Enter student's name: ")
        score_1 = input('First test score: ')
        score_2 = input('Second test score: ')
        score_3 = input('Third test score: ')
        bang_diem.append([name, score_1, score_2, score_3])

        command = input("Do you want to continue [0: yes]: ")
        if command == "0":
            continue
        else: 
            break
    print(bang_diem)
print()
print('Exited.')