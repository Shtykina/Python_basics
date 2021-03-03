class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Maybe drawing some pictures with {self.title}?')


class Pen(Stationery):
    def draw(self):
        print(f'You can draw on the monitor with {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'All right, just follow my {self.title} here.')


class Handle(Stationery):
    def draw(self):
        print(f'We could use stickers and a {self.title} and write the names on.')


stationery = Stationery("stationery")
stationery.draw()
pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()
