def players():
    player_krest = input('Введите имя игрока, играющего кристиком: ')
    player_nol = input('Введите имя игрока, играющего ноликом: ')
    return player_krest, player_nol


def delai_xod():
    while True:
        hod = input('Введите два числа, строка и столбец через пробел: ').split()
        if len(hod) != 2:
            print('Некорректный ввод')
            continue
        elif hod[0] != '0' and hod[0] != '1' and hod[0] != '2':
            print('Некорректный ввод')
            continue
        elif hod[1] != '0' and hod[1] != '1' and hod[1] != '2':
            print('Некорректный ввод')
            continue
        elif game_table[int(hod[0])][int(hod[1])] != '_':
            print('Ячейка занята')
            continue
        else:
            return int(hod[0]), int(hod[1])


def chek_win():
    if game_table[0][0] == game_table[0][1] == game_table[0][2] == mark:
        return True
    elif game_table[1][0] == game_table[1][1] == game_table[1][2] == mark:
        return True
    elif game_table[2][0] == game_table[2][1] == game_table[2][2] == mark:
        return True
    elif game_table[0][0] == game_table[1][0] == game_table[2][0] == mark:
        return True
    elif game_table[0][1] == game_table[1][1] == game_table[2][1] == mark:
        return True
    elif game_table[0][2] == game_table[1][2] == game_table[2][2] == mark:
        return True
    elif game_table[0][0] == game_table[1][1] == game_table[2][2] == mark:
        return True
    elif game_table[0][2] == game_table[1][1] == game_table[2][0] == mark:
        return True
    else:
        return False


def one_more():
    while True:
        one = input('Хотите сыграть еще (да/нет):')
        if one == 'да':
            return True
        elif one == 'нет':
            return False
        else:
            print('Некорректный ответ!')


print('Пора сыграть в крестики-нолики!')

stop_game_flag = True

while stop_game_flag == True:
    pl1, pl2 = players()
    game_table = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    for i in range(1, 11):
        print(f'''  0 1 2

0 {game_table[0][0]} {game_table[0][1]} {game_table[0][2]}

1 {game_table[1][0]} {game_table[1][1]} {game_table[1][2]}

2 {game_table[2][0]} {game_table[2][1]} {game_table[2][2]}''')

        mark = 'x'
        chek = chek_win()
        if chek == True:
            if mark == 'x':
                print('Победил', pl1)
            else:
                print('Победил', pl2)
            break

        if i == 10:
            print('Ничья!')
            ask = one_more()
            if ask == False:
                print('Пока')
                stop_game_flag = False
                break

        if i % 2 == 1:
            mark = 'x'
            print(f'Ход игрока {pl1}')
        else:
            mark = 'o'
            print(f'Ход игрока {pl2}')

        x, y = delai_xod()
        game_table[x][y] = mark

    if stop_game_flag == True:
        ask = one_more()
        if ask == False:
            print('Пока')
            stop_game_flag = False
