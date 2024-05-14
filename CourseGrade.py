'''
    Write a program that reads the student information from a tab separated values (tsv) file.
    The program then creates a text file that records the course grades of the students.
    Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the
    Final score of a student.
    A sample of the student information is provided in StudentInfo.tsv.
    Assume the number of students is at least 1 and at most 20. Assume also the last names and
    first names do not contain whitespaces.

    The program performs the following tasks:
        Read the file name of the tsv file from the user.
        Open the tsv file and read the student information.
        Compute the average exam score of each student.
        Assign a letter grade to each student based on the average exam score in the following scale:
        A: 90 =< x
        B: 80 =< x < 90
        C: 70 =< x < 80
        D: 60 =< x < 70
        F: x < 60
        Compute the average of each exam.
        Output the last names, first names, exam scores, and letter grades of the students into a text
            file named report.txt. Output one student per row and separate the values with a tab character.
        Output the average of each exam, with two digits after the decimal point, at the end of report.txt.
        Hint: Use the format specification to set the precision of the output.

'''
import csv
def student_average(student):
    grades = student[2:]
    total = 0

    for grade in grades:
        total += int(grade)
    average = total / len(grades)

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


file_name = input('Enter file name: ')
midterm1_score = 0
midterm2_score = 0
final_score = 0


with open(file_name) as students:
    reader = csv.reader(students, delimiter='\t')
    row_count = 0
    midterm1_totals = 0
    midterm2_totals = 0
    final_totals = 0

    with open('report.txt', 'w') as report:
        writer = csv.writer(report, delimiter='\t')
        for row in reader:
            row_count += 1
            letter_grade = student_average(row)
            row.append(letter_grade)
            writer.writerow(row)

            midterm1_totals += int(row[2])
            midterm2_totals += int(row[3])
            final_totals += int(row[4])
        midterm1_score = midterm1_totals / row_count
        midterm2_score = midterm2_totals / row_count
        final_score = final_totals / row_count
        report.write('\n')
        final_row = [f'Averages: midterm1 {midterm1_score:.2f}, midterm2 {midterm2_score:.2f}, final {final_score:.2f}']
        writer.writerow(final_row)










