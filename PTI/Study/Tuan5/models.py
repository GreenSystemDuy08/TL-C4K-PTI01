import json
from data_io import load_json_data, write_json_data

class AnimeItem:
    def __init__(self, anime_id, title, release_date, image = None, rating = None, link = None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link
anime = AnimeItem(1, "One Piece", "01/01/2001")

class AnimeDatabase:
    def __init__(self):
        pass
    def items_to_data(self):
        pass
    def load_data(self):
        pass
    def get_first_item_by_title(self, anime_title):
        pass
    def add_item(self, anime_dict):
        pass
    def edit_item(self, edit_title, new_dict):
        pass
    def delete_item(self, delete_title):
        pass
    # def search_by_title(self, search_title) -> list[AnimeItem]:
    #     pass
    def sort_item_by_rating(self, top = None):
        pass
    def sort_item_by_title(self, top = None):
        pass
    def sort_item_by_date(self, top = None):
        pass
    def get_title_list(self):
        pass        

# with open("data.json", "w") as file:
#     json.dump(anime.__dict__, file)