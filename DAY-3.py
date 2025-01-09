## PYTHON PROGRAM TO CALCULATE STUDENT MARKS
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return "Grade: A"
    elif 80 <= average < 90:
        return "Grade: B"
    elif 70 <= average < 80:
        return "Grade: C"
    else:
        return "Grade: Fail"
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
marks = [subject1, subject2, subject3]
print(calculate_grade(marks))