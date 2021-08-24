#python program 1
grade=[]
for i in range(int(input("enter the number of students: "))):
        name=input("enter name: ")
        score=float(input("enter the score: "))
        grade.append([name,score])
sorted_score=sorted(list(set([x[1] for x in grade])))
lowest=sorted_score[1]

low_final=[]
for student in grade:
        if lowest == student[1]:
            low_final.append(student[0])

for student in sorted(low_final):
        print("the student who got second lowest marks is "+ student)


