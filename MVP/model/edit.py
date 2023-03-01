from Classes import Note
from datetime import datetime

edit_choose_string = "Введите id заметки, которую нужно изменить: "

search_error_string = "Заметка не найдена"


def search_note_index(id_note, note_list: list):
    for i in range(len(note_list)):
        if note_list[i].get_id() == int(id_note):
            return i
    return -1

def edit_date(note:Note):
    date = datetime.now()
    date = date.strftime("%d.%m.%Y %H:%M")
    note.set_date(date)


edit_menu_string = "1 - Изменить текст заметки\n" \
                   "2 - Изменить заголовок заметки\n" \
                   "3 - Изменить текст и заголовок заметки\n" \
                   "0 - Назад\n"

edit_menu_choice = "Введите нужный пункт меню: "

successful_change_string = "Заметка успешно изменена!\n"
