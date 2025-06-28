import json

class AnimeItem:
    def __init__(self, id, title, release_date, image=None, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link

anime1 = AnimeItem(1, "One Piece", "01/01/2001")

# with open("anime.json", "w") as file:
#     json.dump(anime1.__dict__, file)

# with open("anime.json", "r") as file:
#     data = json.load(file)
#     load_data = AnimeItem(
#         data["id"],
#         data["title"],
#         data["release_date"],
#     )
# print(load_data.title)

with open("anime_list.json", "r") as file:
    anime_data = json.load(file)
anime_item_list = list()
for item in anime_data:
    anime = AnimeItem(
        id= item["id"],
        title= item["title"],
        release_date= item["release_date"]
    )
    anime_item_list.append(anime)
for item in anime_item_list:
    print(f'Tên Anime: {item.title}')
    print(f'Ra đời: {item.release_date}')
    print('='*15)