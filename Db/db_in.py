from Classes import Note

data_path = "data/note.json"

def save_data(note_list:list):
    with open(data_path, 'w', encoding='UTF-8') as file:
        for note in note_list:
            file.write(f"{note.get_id()};"
                       f"{note.get_date()};"
                       f"{note.get_title()};"
                       f"{note.get_text()}\n")
