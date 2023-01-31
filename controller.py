import model
import view
import os.path

our_stud = ''


def start():
    global our_stud
    while True:
        model.get_path(view.class_choice())
        if os.path.exists(model.path):
            break
        else:
            view.wrong_class()
    model.read_db(model.path)
    while True:
        model.get_subject(view.subject_choice())
        model.get_students_dict(model.journal_lst)
        if model.subject in list(model.journal_dict.keys()):
            break
        else:
            view.wrong_subject()
    view.student_table(model.studs_dict)
    while True:
        inp_student = model.find_student(view.who_answer())
        count = 0
        for stud_db in list(model.studs_dict.keys()):
            if inp_student in str.lower(stud_db):
                count += 1
                our_stud = stud_db
            elif inp_student == '0':
                model.save_mark(model.journal_dict)
                view.save_jornal()
                exit()
        if count == 1:
            while True:
                mark = view.what_mark()
                if mark.isdigit() and 0 < int(mark) < 6:
                    model.studs_dict[our_stud].append(int(mark))
                    break
                else:
                    view.wrong_mark()
        elif count > 1:
            view.few_coincidences()
        else:
            view.wrong_student()
