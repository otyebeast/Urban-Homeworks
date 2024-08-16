grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)

print(type(sorted_students))
print(type(grades))
print(sorted_students)
avg_grades = [float(sum(grades[0])/len(grades[0])),
           float(sum(grades[1])/len(grades[1])),
           float(sum(grades[2])/len(grades[2])),
           float(sum(grades[3])/len(grades[3])),
           float(sum(grades[4])/len(grades[4])), ]
print(avg_grades)
avg_scores = dict(zip(sorted_students, avg_grades))
print(avg_scores)


# st_1 = sorted_students[1], ':', float(sum(grades[1])/len(grades[1]))
# print(st_1)
# st_1 = {''.join(st_1[0:2])}
# print(st_1)

# print(sorted_students[0], sorted_students[1], sorted_students[2], sorted_students[3], sorted_students[4])
# print(grades[0], grades[1], grades[2], grades[3], grades[4],)
# st1_ = (sorted_students[0], ':', float(sum(grades[0])/len(grades[0])))
# print(st1_)
# print(sorted_students[1], ':', float(sum(grades[1])/len(grades[1])))
# avg_scores_1 = {sorted_students[1]: float(sum(grades[1])/len(grades[1]))}
# print(avg_scores_1)


