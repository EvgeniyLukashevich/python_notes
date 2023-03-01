from Db import load_data, save_data
from .view import show_menu, select_menu_item, show_notes, \
    add_text, add_title, \
    edit_choose, search_error, edit_menu, select_edit_item, successful_change,\
    successful_remove
from .model import menu_string, select_menu_string, show_notes_string, \
    add_text_string, add_title_string, add_note_to_notelist, \
    edit_choose_string, search_note_index, search_error_string, \
    edit_menu_string, edit_menu_choice, successful_change_string, edit_date, \
    remove_choose_string, successful_remove_string


def start():
    note_list = load_data()

    while True:
        show_menu(menu_string)
        user_choice = select_menu_item(select_menu_string)

        if user_choice == "1":
            show_notes(show_notes_string(note_list))
        elif user_choice == "2":
            title = add_title(add_title_string)
            text = add_text(add_text_string)
            note_list = add_note_to_notelist(title=title,
                                             text=text,
                                             note_list=note_list)
            save_data(note_list)
        elif user_choice == "3":
            show_notes(show_notes_string(note_list))
            try:
                note_id = edit_choose(edit_choose_string)
                index = search_note_index(id_note=note_id, note_list=note_list)
            except:
                index = -1
            if index == -1:
                search_error(search_error_string)
                continue
            edit_menu(edit_menu_string)
            user_edit_choice = select_edit_item(edit_menu_choice)
            if user_edit_choice == '1':
                text = add_text(add_text_string)
                edit_date(note_list[index])
                note_list[index].set_text(text)
            elif user_edit_choice == '2':
                title = add_title(add_title_string)
                edit_date(note_list[index])
                note_list[index].set_title(title)
            elif user_edit_choice == '3':
                text = add_text(add_text_string)
                title = add_title(add_title_string)
                edit_date(note_list[index])
                note_list[index].set_text(text)
                note_list[index].set_title(title)
            else:
                continue
            save_data(note_list)
            successful_change(successful_change_string)

        elif user_choice == "4":
            show_notes(show_notes_string(note_list))
            try:
                note_id = edit_choose(remove_choose_string)
                index = search_note_index(id_note=note_id, note_list=note_list)
            except:
                index = -1
            if index == -1:
                search_error(search_error_string)
                continue
            note_list.remove(note_list[index])
            save_data(note_list)
            successful_remove(successful_remove_string)
        if user_choice == '0':
            return 1
