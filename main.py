from colorama import Fore, Back, Style, init

# Инициализация Colorama с автоматическим сбросом цветов
init(autoreset=True)


def draw_board(board):
    """Отображает игровое поле с цветными символами."""

    # Перебираем строки игрового поля
    for i in range(3):
        colored_row = []

        # Перебираем клетки текущей строки
        for j in range(3):
            cell = board[i][j]

            # Красный цвет для X
            if cell == "X":
                colored_row.append(Fore.RED + cell + Fore.RESET)

            # Синий цвет для O
            elif cell == "O":
                colored_row.append(Fore.BLUE + cell + Fore.RESET)

            # Жёлтый фон для пустых клеток
            else:
                colored_row.append(Back.YELLOW + cell + Back.RESET)

        # Выводим строку с цветными символами
        print(" | ".join(colored_row))

        # Разделитель между строками, кроме последней
        if i < 2:
            print("---------")


def ask_and_make_move(player, board):
    """Запрашивает координаты и выполняет ход игрока."""

    # Получаем проверенные координаты
    x, y = ask_move(player, board)

    # Записываем символ игрока в выбранную клетку
    make_move(player, board, x, y)


def ask_move(player, board):
    """Запрашивает координаты до получения корректного хода."""

    # Повторяем запрос, пока игрок не введёт правильные координаты
    while True:
        try:
            # Получаем два значения и преобразуем их в числа
            x, y = input(
                f"{player}, enter x and y coordinates (e.g. 0 0): "
            ).strip().split()

            x, y = int(x), int(y)

        except ValueError:
            # Обрабатываем неправильный ввод
            print("Please enter two valid numbers")
            continue

        # Проверяем границы поля и доступность клетки
        if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
            return (x, y)
        else:
            print("Клетка занята. Введите координаты еще раз.")


def make_move(player, board, x, y):
    """Размещает символ игрока в выбранной клетке."""

    # Запрещаем ход в занятую клетку
    if board[x][y] != " ":
        print("Клетка занята")
        return False

    # Записываем X или O в игровое поле
    board[x][y] = player
    return True


def check_win(player, board):
    """Проверяет, собрал ли игрок три символа в ряд."""

    for i in range(3):

        # Проверка горизонтальных линий
        if board[i] == [player, player, player]:
            return True

        # Проверка вертикальных линий
        if (
            board[0][i] == player
            and board[1][i] == player
            and board[2][i] == player
        ):
            return True

    # Проверка главной диагонали: слева сверху направо вниз
    if (
        board[0][0] == player
        and board[1][1] == player
        and board[2][2] == player
    ):
        return True

    # Проверка побочной диагонали: справа сверху налево вниз
    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
    ):
        return True

    # Ни одна выигрышная комбинация не найдена
    return False


def check_draw(board):
    """Проверяет, заполнены ли все клетки игрового поля."""

    # Перебираем все строки и клетки
    for row in board:
        for cell in row:

            # Если есть пустая клетка, игра может продолжаться
            if cell == " ":
                return False

    # Свободных клеток не осталось
    return True


def tic_tac_toe():
    """Управляет игровым процессом и повторными партиями."""

    # Внешний цикл позволяет начинать новые партии
    while True:

        # Создаём пустое игровое поле 3×3
        board = [[" " for i in range(3)] for j in range(3)]

        # Первым ходит игрок X
        player = "X"

        # Основной цикл ходов текущей партии
        while True:

            # Показываем поле перед ходом
            draw_board(board)

            # Запрашиваем и выполняем ход
            ask_and_make_move(player, board)

            # Проверяем победу текущего игрока
            if check_win(player, board):
                print(f"{player} you wins!")
                draw_board(board)
                break

            # Проверяем ничью, если победителя нет
            if check_draw(board):
                print("Ничья!")
                draw_board(board)
                break

            # Передаём ход другому игроку
            player = "O" if player == "X" else "X"

        # Предлагаем начать новую партию
        restart = input("Хотите сыграть еще раз? (y/n) ")

        # Любой ответ, кроме y, завершает программу
        if restart.lower() != "y":
            break


# Точка запуска игры
tic_tac_toe()