class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, creation_year):
        self.title = title
        self.painter = painter
        self.creation_year = creation_year

        print(f"\"{self.title}\" by {self.painter} ({self.creation_year}) hangs in the {Painting.museum}.")


title_input = input()
painting_input = input()
year_input = int(input())
painting = Painting(title_input, painting_input, year_input)
