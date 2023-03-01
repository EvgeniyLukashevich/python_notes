from Classes import Note

data_path = "data/note.json"


def load_data():
    note_list = []
    try:
        with open(data_path, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                note_line = line.strip().split(';')
                note = Note()
                note.set_id(note_id=int(note_line[0]))
                note.set_date(str(note_line[1]))
                note.set_title(title=note_line[2])
                note.set_text(text=note_line[3])
                note_list.append(note)
    except:
        return "Db error"
    return note_list
