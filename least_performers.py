def find_kannada_least_performer(student_list):
    least_marks_in_kannada = 100
    least_performer_in_kannada = ""
    for student in student_list:
        if student.get("Kannada") < least_marks_in_kannada:
            least_marks_in_kannada = student.get("Kannada")
            least_performer_in_kannada = student.get("Name")
    return f"{least_performer_in_kannada} secured least marks = {least_marks_in_kannada} " \
           f"in Kannada!\nPlease work hard {least_performer_in_kannada}!"


def find_english_least_performer(student_list):
    least_marks_in_english = 100
    least_performer_in_english = ""
    for student in student_list:
        if student.get("English") < least_marks_in_english:
            least_marks_in_english = student.get("English")
            least_performer_in_english = student.get("Name")
    return f"{least_performer_in_english} secured least marks = {least_marks_in_english} " \
           f"in English!\nTry hard to get more marks {least_performer_in_english}!"


def find_hindi_least_performer(student_list):
    least_marks_in_hindi = 100
    least_performer_in_hindi = ""
    for student in student_list:
        if student.get("Hindi") < least_marks_in_hindi:
            least_marks_in_hindi = student.get("Hindi")
            least_performer_in_hindi = student.get("Name")
    return f"{least_performer_in_hindi} secured highest marks = {least_marks_in_hindi} " \
           f"in Hindi!\nPlease work hard {least_performer_in_hindi}!"


def find_maths_least_performer(student_list):
    least_marks_in_maths = 100
    least_performer_in_maths = ""
    for student in student_list:
        if student.get("Maths") < least_marks_in_maths:
            least_marks_in_maths = student.get("Maths")
            least_performer_in_maths = student.get("Name")
    return f"{least_performer_in_maths} secured highest marks = {least_marks_in_maths} " \
           f"in Maths!\nPlease work hard {least_performer_in_maths}!"


def find_science_least_performer(student_list):
    least_marks_in_science = 100
    least_performer_in_science = ""
    for student in student_list:
        if student.get("Science") < least_marks_in_science:
            least_marks_in_science = student.get("Science")
            least_performer_in_science = student.get("Name")
    return f"{least_performer_in_science} secured highest marks = {least_marks_in_science} " \
           f"in Science!\nPlease work hard {least_performer_in_science}!"


def find_socialscience_least_performer(student_list):
    least_marks_in_socialscience = 100
    least_performer_in_socialscience = ""
    for student in student_list:
        if student.get("Social Science") < least_marks_in_socialscience:
            least_marks_in_socialscience = student.get("Social Science")
            least_performer_in_socialscience = student.get("Name")
    return f"{least_performer_in_socialscience} secured h" \
           f" marks = {least_marks_in_socialscience} " \
           f"in Social Science!\nPlease work hard {least_performer_in_socialscience}!"
