from bs4 import BeautifulSoup

import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
content = response.text
# print(content)

soup = BeautifulSoup(content, "html.parser")
mov = soup.find_all(name="h3", class_="title")
# print(mov)
movie_title = [movie.getText() for movie in mov]
more_mov = movie_title[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for mo in more_mov:
        file.write(f"{mo}\n")

















# with open("index.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="header")
# # print("heading")
# # heading = soup.find(name="h1", class_="")
#
# company_url = soup.select_one(selector="p a")
# print(company_url)