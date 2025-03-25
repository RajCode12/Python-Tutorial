# student list
student_database = []

# function to add student in the database
def add_student(rollno,name,age,grade,score):
    dict1 = {'rollno':rollno, 'name':name, 'age':age, 'grade':grade, 'score':score}
    student_database.append(dict1)
    print('Student with roll number ', rollno, ' added to the database.')

# function to search student in the database
def search_student(roll):
    flag = False
    for student in student_database:
        if student.get('rollno') == roll:
            flag = True
            print(student)
            return student
    if flag == False:
        print('Student with roll number ', roll, ' not found in the database.')
    return None

# function to remove student in the database
def remove_student(roll):
    student = search_student(roll)
    if student:
        student_database.remove(student)
        print('Student with roll number ', roll, ' removed from the database')
    
# function to update student in the database
def update_student(roll,name=None,age=None,grade=None,score=None):
    student = search_student(roll)
    if student:
        if name:
            student['name'] = name 
        if age:
            student['age'] = age 
        if grade:
            student['grade'] = grade
        if score:
            student['score'] = score
        print('Student with roll number ', roll, ' updated.')

# function to display all students in the database
def display_student():
    for student in student_database:
        print(student)
    
# function to calculate average score of students in the database
def calculate_average_score():
    length = len(student_database)
    score_sum = 0
    for student in student_database:
        score_sum += student.get('score')
    print('Average score : ', score_sum/length)
    
# Test cases 
    
add_student(1,'John Doe',20,3,85)
add_student(2,'Jay',21,3,90)
add_student(3,"Jane Doe",22,4,90)
print('********************************************')

remove_student(1)

display_student()
print('********************************************')

update_student(2,'Eshan',33,2,99)
print('********************************************')

search_student(2)
search_student(5)
print('********************************************')

calculate_average_score()



