grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gr_of_stud = {}
students = sorted(list(students))
for i in range(len(students)):
    gr_of_stud[students[i]]=sum(grades[i])/len(grades[i])
print(gr_of_stud)