class Note:
    __note_id: int
    __date: str
    __title: str
    __text: str

    def __init__(self):
        self.__note_id = 9999
        self.__date = "01.01.0001 00:00"
        self.__title = "Заголовок отсутствует"
        self.__text = "Текст отсутствует"

    def set_id(self, note_id: int):
        self.__note_id = note_id

    def set_date(self, date: str):
        self.__date = date

    def set_title(self, title: str):
        self.__title = title

    def set_text(self, text: str):
        self.__text = text

    def get_id(self):
        return self.__note_id

    def get_date(self):
        return self.__date

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text
