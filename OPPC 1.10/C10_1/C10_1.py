class Circle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def GetInf(self):
        return print("Circle ({0}, {1}, {2}, {3}). ".format(self.x, self.y, self.width, self.height))


class Recktangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def GetInf(self):
        return print("Recktangle ({0}, {1}, {2}, {3}). ".format(self.x, self.y, self.width, self.height))