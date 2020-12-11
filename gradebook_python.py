# You are a student and you are trying to organize your subjects and grades using Python. 

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]


subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append("100")

gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
print(gradebook)
# [('physics', 98), ('calculus', 97), ('poetry', 85), ('history', 88), ('computer science', '100'), ('visual arts', 93)]

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
# [('politics', 80), ('latin', 96), ('dance', 97), ('architecture', 65), ('physics', 98), ('calculus', 97), ('poetry', 85), ('history', 88), ('computer science', '100'), ('visual arts', 93)]

# For reference: https://www.youtube.com/watch?v=jJj0WWYxmbY
