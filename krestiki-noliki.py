field = [[" "] * 3  for i in range(3)]

def show_grid():
    print(f"____0___1___2__")
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("_______________")
def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")

def ask_cords():
    while True:
        cords = input("Введите координаты Х и У: ").split()
        if len(cords) != 2:
            print("Введите еще раз Х и У")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)

        if 0 < x > 2 or   0 < y > 2 :
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != ' ':
            print("Клетка занята, выберите другую")
            continue
        return x,y
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

greet()

count = 0
while True:
    count += 1
    show_grid()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask_cords()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break
    if count == 9:
        print(" Ничья!")
        break





