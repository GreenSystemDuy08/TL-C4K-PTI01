class NoteApp():
    def __init__(self, Note_id, title, release_date, language, rating):
        self.id = Note_id
        self.title = title
        self.release_date = release_date
        self.language = language
        self.rating = rating if rating else 0
    def update(self, new_data:dict):
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)
    def duyet_phan_tu():
        for Note in Notes:
            print(Note.title)
    def xoa_phan_tu():
        remove_title = input("Nhập tiêu đề cần xóa: ")
        for Note in Notes:
            if Note.title == remove_title:
                Notes.remove(Note)
    def update_note():
        Note1 = NoteApp(1, "Hello e vờ ri quan", "29/3/2024", "English", "Good")
        new_data = {"title": "Hello everyone"}
        Note1.update(new_data)
        print(Note1.title)
        print(Note1.release_date)

Note1 = NoteApp(1, "Hello e vờ ri quan", "29/3/2024", "English", "Good")
Note2 = NoteApp(2, "Tôi là Duy", "1/4/2024", "Vietnamese", "Good")
Note3 = NoteApp(3, "NoteApp này rất tuyệt vời!", "31/3/2024", "English", "Good")
Note4 = NoteApp(4, "Note này chưa Save được", "29/3/2024", "French", "Bad")
Note5 = NoteApp(5, "Chia sẻ được online", "30/3/2024", "Japanese", "WOW!")
Notes = [Note1, Note2, Note3, Note4, Note5]
Note6 = NoteApp(1, "Conan", "1/1/1990", "Korean", "Ok")
Notes.append(Note6)
NoteApp.duyet_phan_tu()
NoteApp.xoa_phan_tu()
NoteApp.duyet_phan_tu()
NoteApp.update_note()

class NoteAppList():
    def __init__(self):
        self.note_item_list = list()
    def get_item_by_title(self, NoteApp_title) -> NoteApp:
        pass
    def add_new_item(self, NoteApp):
        pass
    def edit_item(self, edit_title, Notes: NoteApp):
        pass
    def delete_item(self,delete_title):
        pass
