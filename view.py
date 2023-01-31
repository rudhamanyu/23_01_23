import controller


def class_choice():
    return input('Какой класс? ').upper()


def wrong_class():
    print('Такого класса нет.')


def wrong_subject():
    print('Такого предмета нет.')


def wrong_student():
    print('Такого ученика нет.')


def wrong_mark():
    print('Введите корректную оценку.')


def subject_choice():
    return input('Введите предмет: ').lower()


def student_table(studs_dict: dict):
    for k, v in studs_dict.items():
        print(f'{k:20} {v}')


def who_answer():
    return input('\nВведите фамилию ученика, либо "0" для сохранения и выхода: ')


def save_jornal():
    print('Изменения сохранены.\nЗавершение программы.')


def what_mark():
    return input(f'На какую оценку ответил {controller.our_stud}? ')


def few_coincidences():
    print('Нашлось несколько совпадений, введите более точный запрос.')