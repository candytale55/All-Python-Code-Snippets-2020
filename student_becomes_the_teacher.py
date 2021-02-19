# Python 2



# STUDENT FILES:

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}






# function AVERAGE

def average(numbers):
  total = float(sum(numbers)) / float(len(numbers))
  return total

# Test: Average
print  "Test function average:"
print "Tyler's homework: " + str(average(tyler["homework"]))
print "Alice's homework: " + str(average(alice["homework"]))

print ""





#  function GET_AVERAGE

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (homework * 0.10) + (quizzes * 0.30) + (tests * 0.60)


# Tests get_average
print "Weighted average:"
print "Lloyd's : " + str(get_average(lloyd)) # 80.55
print "Alice's :" + str(get_average(alice)) # 91.15
print "Tyler's: " + str(get_average(tyler)) # 79.09

"""
print get_average(lloyd) # 80.55
print get_average(alice) # 91.15
print get_average(tyler) # 79.09
"""




# function GET_LETTER_GRADE

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"


print ""
print "Letter Grade:"
print "Lloyd: " + (get_letter_grade(get_average(lloyd))) # B
print "Alice: " + (get_letter_grade(get_average(alice))) # A
print "Tyler: " + (get_letter_grade(get_average(tyler))) # C

print ""



# function GET_CLASS_AVERAGE


def get_class_average(class_list):
  results = []
  for each_student in class_list:
    results.append(get_average(each_student))
  return average(results)


# STUDENT LIST
students = [lloyd, alice, tyler]



# Find the average grade of the class.
print "Class average: " + str((get_class_average(students))) # 83.866...

# determine the letter grade for the class’s average
print "Class letter grade: " + get_letter_grade(get_class_average(students)) #




# FOR REFERENCE: 
# REF: https://discuss.codecademy.com/t/why-are-my-student-dictionaries-not-accepted/339215
# https://discuss.codecademy.com/t/why-do-these-scores-need-to-be-saved-as-floats/339216
# https://discuss.codecademy.com/t/do-i-need-to-make-students-a-list-of-their-string-names-or-the-variable-names/339218
# https://discuss.codecademy.com/t/what-is-codecademy-checking-for-to-be-printed/339219
# https://discuss.codecademy.com/t/why-is-my-returned-average-value-incorrect/339220
# https://discuss.codecademy.com/t/how-can-i-calculate-a-weighted-average/339223
# https://discuss.codecademy.com/t/how-can-i-test-my-get-letter-grade-function/339226
# https://discuss.codecademy.com/t/why-is-the-average-returned-incorrect/339227
# https://discuss.codecademy.com/t/why-does-it-run-into-issues-when-running-my-code/339228
