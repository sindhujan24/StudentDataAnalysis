"""
This project is to analyse the student records
provided by the respective institutions.
And displaying the student information, who has secured highest and least marks
in each subjects. Assuming each student has secured unique marks.
"""
from student_records import student_record_list
from best_performers import find_english_topper, \
    find_hindi_topper, find_kannada_topper, \
    find_maths_topper, find_science_topper, \
    find_socialscience_topper

from least_performers import find_kannada_least_performer, \
    find_english_least_performer, find_hindi_least_performer, \
    find_science_least_performer, find_maths_least_performer, \
    find_socialscience_least_performer

print("1. Display Best Performers in each subject\n"
      "2.Display Least Performers in each subject")
choice = int(input("Please enter your choice"))

try:
    if choice == 1:
        print(find_kannada_topper(student_record_list))
        print(find_english_topper(student_record_list))
        print(find_hindi_topper(student_record_list))
        print(find_maths_topper(student_record_list))
        print(find_science_topper(student_record_list))
        print(find_socialscience_topper(student_record_list))
    else:
        print(find_kannada_least_performer(student_record_list))
        print(find_english_least_performer(student_record_list))
        print(find_hindi_least_performer(student_record_list))
        print(find_maths_least_performer(student_record_list))
        print(find_science_least_performer(student_record_list))
        print(find_socialscience_least_performer(student_record_list))
except ValueError:
    print("Please enter valid choice 1 or 2")
