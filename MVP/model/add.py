from Classes import Note
from datetime import datetime

add_title_string = "Введите заголовок заметки: "

add_text_string = "Введите текст заметки: "


def add_note_to_notelist(title: str, text: str, note_list: list):
    if len(note_list) == 0:
        note_id = 1
    else:
        note_id = note_list[-1].get_id() + 1
    date = datetime.now()
    date = date.strftime("%d.%m.%Y %H:%M")
    note = Note()
    note.set_id(note_id)
    note.set_date(date)
    note.set_title(title)
    note.set_text(text)
    note_list.append(note)
    return note_list
