# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing. 

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg <90:
    letter_grade = "B"
elif avg > 69 and avg <80:
    letter_grade = "C"
elif avg <= 69 and avg >=65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
#The average and grade should be based on the all the exams.  The  indentation here causes the last two print statements to get included in the loop.  Remove the indentation from that 
#second and third print statements.
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")

#Removed the additional letter "i" for "Student is failing" on line 20
#Changed "exam_3" to "exam_three" on line 26
#Added "int(" "to exam_two =" on line 24
#Changed the "str" function to "int" on line 26
#Added an "s" to the word grades on line 30
#Added an "s" to the word grades on line 33    
#Changed "elif" to "else" on line 43
#Added an "s" to the word grades on line 46
#Changed "is" to "==" on line 53 based on sytax warning

