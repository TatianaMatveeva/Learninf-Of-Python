class Guests:
    def __init__(self, name, location, status):
        self.name = name
        self.location = location
        self.status = status


class Human(Guests):
    def get_person(self):
        return f'''{self.name}, {self.location}, stile IN life "{self.status}"'''


Vol1 = Human('Джони пуля в зубах', 'Москва', 'Киллер')
Vol2 = Human('Адель черная душа', 'Смольный', 'Черный Риэлтор')
Vol3 = Human('Один раз не программист', 'Зеленоград', 'Голодный студент')
volunteers = [Vol1, Vol2,Vol3]
for i in volunteers:
    print(i.get_person())