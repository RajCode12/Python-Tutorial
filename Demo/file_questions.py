# 1 

import csv

with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

average_age = sum(int(row['age']) for row in rows) / len(rows)
highest_grade_student = max(rows, key=lambda x: int(x['grade']))

print(f"Average age of all students: {average_age}")
print(f"Student(s) with the highest grade: {highest_grade_student['name']} ({highest_grade_student['grade']})")

print("\nData for all students:")
for row in rows:
    print(row)

# 2

FILENAME = "article.txt"

def search_word():
    word = input("Enter the word to search for: ").strip()
    
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        found = False
        for i, line in enumerate(lines, start=1):
            if word in line:
                print(f"Line {i}: {line.strip()}")
                found = True
        
        if not found:
            print(f"'{word}' not found in the file.")
    
    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found.")

# 3



