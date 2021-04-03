# Для AI
from random import randint

# cодержит в себе остальные классы исключений
class BoardException(Exception):  # класс родитель всех исключений
    pass
# исключения, если пользователь стреляет за границы доски
class BoardOutException(BoardException):
    def __str__(self):
        return "Ты стреляешь за границы доски, придерживайся правил!!!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Ты уже стрелял сюда"

class BoardWrongShipException(BoardException): # если пользователь пытается поставить корабль на доску в недопустимое место
    pass

# собственный тип данных "точка" два параметра в конструкторе
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # отвечает за сравнение двух аргументов x and y на равенство
        return self.x == other.x and self.y == other.y

    # отвечает за строковое представление объекта в консоле,
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

# Создаем корабли
class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property  # метод вычисляет свойство для корабля
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y)) #

        return ship_dots

    def shooten(self, shot): # покажет попадаем ли мы корабль
        return shot in self.dots

# Cоздаём доску
class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)] # храним состояние

        self.busy = []   # список занятый клеток
        self.ships = []  # список кораблей доски

    def add_ship(self, ship): # проверяем статус корабля

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship) # собственные корабли
        self.contour(ship)

    def contour(self, ship, verb=False): # в списке near содержит сдвиги
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots: # каждую точку корабля в цикле и проходим все списки
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

# переменная res записывает всю нашу доску
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field): # цикл проходит по строкам доски
            res += f"\n{i + 1} | " + " | ".join(row) + " |"  # выводим номер строки и клетки

        if self.hid: # отвечает за корабли
            res = res.replace("■", "O")
        return res

    def out(self, d): # метод проверяющий выходит ли точка за рамки доски
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d): # стреляем по кораблю
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships: # цикл проверки кораблей
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "#"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True) # точки вокруг корабля
                    print("Убил!!")
                    return False
                else:
                    print("Ранил!!")
                    return True # повторить ход после поражения

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = [] # для хранения результата после хода
    def defeat(self):
        return self.count == len(self.ships)

# Создаем игрока AI и игрока человека
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask() # координаты
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5)) #
        print(f"Ходит компьютер: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Xоди: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)

# генерация досок
class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000: # попытки создания доски
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin() # подготовим кораблей
        return board

    def greet(self):
        print("-----------------------------------")
        print("  Добро пожаловать в Battleship!!  ")
        print("-----------------------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def print_board(self):
        print("-" * 20)
        print("Доска пользователя:")
        print(self.us.board)
        print("-" * 20)
        print("Доска компьютера:")
        print(self.ai.board)

    def loop(self):
        num = 0
        while True:
            self.print_board()
            if num % 2 == 0: # жеребьевка
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.defeat(): # кол-во кораблей на доске
                self.print_board()
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                self.print_board()
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self): # метод старт
        self.greet()
        self.loop()


g = Game()
g.start() # вызываем метод функции