# %%
from bs4 import BeautifulSoup

with open("basic_scraping.html", "r") as html_file:
    contents = html_file.read()

    soup = BeautifulSoup(contents, "lxml")

    course_cards = soup.find_all("div",class_="card")
    for course in course_cards:
      course_name = course.h5.text
      course_price = course.a.text.split()[-1]
      print(f"Course Name:: {course_name}\tCourse Price:: {course_price}")
  # %%
