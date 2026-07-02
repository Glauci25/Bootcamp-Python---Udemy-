'''
with open("file1.txt", "r") as file1:
    lista1 = [int(name.strip()) for name in file1.readlines()]

with open("file2.txt", "r") as file2:
    lista2 = [int(name.strip()) for name in file2.readlines()]

result = [n for n in lista1 if n in lista2]

print(result)
'''
'''
import random
list_of_names = ['Anna', 'Beth', 'Carol', 'Daniela', 'Elena', 'Freddie', 'Glamour']
students_scores = {student: random.randint(1,100) for student in list_of_names}
print(students_scores)

passed_students = {
    student: score for (student,score) in students_scores.items() if score > 60
}
print(passed_students)
'''
'''
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

list_f = []
for key,temp in weather_c:
    temp_f = 32+(temp[key])
    list_f.append(temp_f)

print(list_f)

weather_f = {
    day: f for (day,f) in weather_c.items()
}

print(weather_f)
'''

import pandas

#usando pandas.DataFrame pra mostrar uma tabelinha de acordo com o dicionário
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56,76,98]
}
student_data_frame =pandas.DataFrame(student_dict)
print(student_data_frame)

#loop no dataframe
for (key,value) in student_data_frame.items():
    print(value)

#loop pelas linhas de um dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.scores)
