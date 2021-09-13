def find_kannada_topper(student_list):
    highest_marks_in_kannada = 0
    topper_in_kannada = ""
    for student in student_list:
        if student.get("Kannada") > highest_marks_in_kannada:
            highest_marks_in_kannada = student.get("Kannada")
            topper_in_kannada = student.get("Name")
    return f"{topper_in_kannada} secured highest marks = {highest_marks_in_kannada} " \
           f"in Kannada!\nCongratulation {topper_in_kannada}!"


def find_english_topper(student_list):
    highest_marks_in_english = 0
    topper_in_english = ""
    for student in student_list:
        if student.get("English") > highest_marks_in_english:
            highest_marks_in_english = student.get("English")
            topper_in_english = student.get("Name")
    return f"{topper_in_english} secured highest marks = {highest_marks_in_english} " \
           f"in English!\nCongratulation {topper_in_english}!"


def find_hindi_topper(student_list):
    highest_marks_in_hindi = 0
    topper_in_hindi = ""
    for student in student_list:
        if student.get("Hindi") > highest_marks_in_hindi:
            highest_marks_in_hindi = student.get("Hindi")
            topper_in_hindi = student.get("Name")
    return f"{topper_in_hindi} secured highest marks = {highest_marks_in_hindi} " \
           f"in Hindi!\nCongratulation {topper_in_hindi}!"


def find_maths_topper(student_list):
    highest_marks_in_maths = 0
    topper_in_maths = ""
    for student in student_list:
        if student.get("Maths") > highest_marks_in_maths:
            highest_marks_in_maths = student.get("Maths")
            topper_in_maths = student.get("Name")
    return f"{topper_in_maths} secured highest marks = {highest_marks_in_maths} " \
           f"in Maths!\nCongratulation {topper_in_maths}!"


def find_science_topper(student_list):
    highest_marks_in_science = 0
    topper_in_science = ""
    for student in student_list:
        if student.get("Science") > highest_marks_in_science:
            highest_marks_in_science = student.get("Science")
            topper_in_science = student.get("Name")
    return f"{topper_in_science} secured highest marks = {highest_marks_in_science} " \
           f"in Science!\nCongratulation {topper_in_science}!"


def find_socialscience_topper(student_list):
    highest_marks_in_socialscience = 0
    topper_in_socialscience = ""
    for student in student_list:
        if student.get("Social Science") > highest_marks_in_socialscience:
            highest_marks_in_socialscience = student.get("Social Science")
            topper_in_socialscience = student.get("Name")
    return f"{topper_in_socialscience} secured highest marks = {highest_marks_in_socialscience} " \
           f"in Social Science!\nCongratulation {topper_in_socialscience}!"
