path = ''
subject = ''
journal_lst = []
journal_dict = {}
studs_dict = {}


def get_path(class_choice: str):
    global path
    path = 'Classes/' + class_choice + '.txt'


def get_subject(input_sub: str):
    global subject
    subject = input_sub


def read_db(path_data: str):
    global journal_lst
    with open(path_data, 'r', encoding='UTF-8') as data:
        journal_lst = data.readlines()
    return journal_lst


def get_students_dict(journal: list):
    global journal_dict
    global studs_dict
    for line in journal:
        line_journal = line.strip().split(';')
        if subject == line_journal[0]:
            studs_list = line_journal[1].split('&')
            for i, stud in enumerate(studs_list):
                stud_list = studs_list[i].split('-')
                studs_dict[stud_list[0]] = list(map(int, stud_list[1].split(',')))
            journal_dict[line_journal[0]] = studs_dict
    return studs_dict


def find_student(input_student: str):
    inp_stud = str.lower(input_student)
    return inp_stud


def save_mark(new_dict: dict):
    str_sub = list(new_dict.keys())[0] + ';'
    str_studs = ''
    for k, v in studs_dict.items():
        str_studs += k + '-' + ','.join(map(str, v)) + '&'
    new_line = str_sub + str_studs
    new_line = new_line[:-1] + '\n'

    for i, line in enumerate(journal_lst):
        if line.split(';')[0] == subject:
            journal_lst[i] = new_line

    with open(path, 'w', encoding='UTF-8') as data:
        data.write(''.join(journal_lst))
