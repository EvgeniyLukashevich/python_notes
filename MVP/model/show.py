from Classes import Note

menu_string = "---------------------------\n" \
              "1 - Посмотреть заметки\n" \
              "2 - Добавить заметку\n" \
              "3 - Редактировать заметку\n" \
              "4 - Удалить заметку\n" \
              "0 - Выйти\n"

select_menu_string = "Выберите пункт меню: "


def show_notes_string(note_list: list):
    string = "Ваши заметки:\n\n"
    for note in note_list:
        note: Note
        string += f"id: {note.get_id()}\n" \
                  f"{note.get_date()}\n" \
                  f"{note.get_title()}\n" \
                  f"{note.get_text()}\n\n"
    return string
