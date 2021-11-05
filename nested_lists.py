if __name__ == '__main__':
    students = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    second_min_score = sorted(list(set([thing[1] for thing in sorted(students, key=lambda x:x[1])])))[1]

    students = sorted(students, key=lambda x:x[0])
    
    for i in range(len(students)):
        if students[i][1] == second_min_score: print(students[i][0])
