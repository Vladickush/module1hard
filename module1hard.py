grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Необходимо составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

students_list = sorted (students)  # сортированный список студентов

end = len (grades)
students_dict = {}
i = 0
while i < end:
        students_dict [students_list[i]] = sum (grades[i]) / len (grades[i])
        i = i + 1
else:
        print(students_dict)