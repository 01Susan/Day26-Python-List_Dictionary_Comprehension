import random
import pandas as pd
# Format for Dictionary Comprehension using list
# new_dict = {new_key : new_value for items in list}

names = ["Susan", "Aashutosh", "Gunjan"]
student_score = {student_name: random.randint(0, 100) for student_name in names}
print(student_score)

# Format for Dictionary Comprehension using list
# new_dict = {new_key : new_value for (key,value) in dictionary.items}
passed_student = {student: score for (student, score) in student_score.items() if score > 75}
print(passed_student)
