from bin import Kino
from bin import Kinotheatr

comand = 0
comand2 = 0
theatrList = []
filmList = []
nearest = [0]
flagCommand = ''
num = -1
name = ''


def update():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


while True:
    update()
    print(flagCommand)
    flagCommand = ''
    if comand == 0:
        try:
            if len(theatrList) == 0:
                print('Кинотеатров нет')
            comand = int(input('Список кинотеатров (1)\nБлижайший сеанс (2)\nДобавить фильм (3)\nДобавить кинотеатр (4)\n'))
        except ValueError:
            flagCommand = '! Введите только цифру'

    if comand == 1:
        for n, i in enumerate(theatrList):
            print(n + 1, i.name)

        if len(theatrList) == 0:
            comand = 0
            continue
        try:
            comand2 = int(input('Введите номер выбранного кинотеатра (для выхода введите -1)'))
        except ValueError:
            flagCommand = '! Введите только цифру'

        if comand2 == -1:
            comand = 0
            continue
        nowTheatr = theatrList[comand2 - 1]

        try:
            comand2 = int(input('Добавить зал (1)\nДобавить сеанс (2)\nДля выхода введите -1'))
        except ValueError:
            flagCommand = '! Введите только цифру'

        if comand2 == -1:
            comand = 0
            continue
        elif comand2 == 1:
            with open('map.txt', mode='rt') as f:
                mp = f.readlines()
                for i in mp:
                    print(i, end='')
            path = input('Введите полный путь к карте (в формате .txt)\n')
            nowTheatr.add_zal(nowTheatr, path)
        elif comand2 == 2:
            for i in range(nowTheatr.zalList):
                print(i + 1)
            if num == -1:
                try:
                    num = int(input('Введите номер зала (только число)\n'))
                except ValueError:
                    flagCommand = '! Введите только цифру'
                    continue
                nowTheatr.zalList[num - 1].print_map()
                try:
                    num = int(input(f'Подтвердите номер выбранного зала! Нынешний номер: {num}'))
                except ValueError:
                    flagCommand = '! Введите только цифру'
                    continue
                nowTheatr.zalList[num - 1].print_map()
                for i, elem in enumerate(filmList):
                    print(i + 1, f'Название: {elem.name}, Длительность: {elem.duration}')
            try:
                film = int(input('Введите номер выбранного фильма\n'))
            except ValueError:
                flagCommand = '! Введите только цифру'
                continue
            try:
                film = int(input('Подтвердите номер выбранного фильма\n'))
            except ValueError:
                flagCommand = '! Введите только цифру'
                continue
            time_start = input('Введите дату и время начала сеанса в формате: Месяц/День/Год Час:Минута\n')
            if len(time_start.split('/')) != 3 or len(time_start.split('/')[2].split(' ')) != 2 or  len(time_start.split('/')[2].split(' ')[1].split(':')) != 2:
                flagCommand = '! Введите дату и время в указанном формате!'
                continue
            time_start = input('Подтвердите дату и время начала сеанса в формате: Месяц/День/Год Час:Минута\n')
            if len(time_start.split('/')) != 3 or len(time_start.split('/')[2].split(' ')) != 2 or len(
                    time_start.split('/')[2].split(' ')[1].split(':')) != 2:
                flagCommand = '! Введите дату и время в указанном формате!'
                continue
            nowTheatr.zalList[num - 1].add_kino(filmList[film - 1], time_start)
            num = -1


    if comand == 2:
        if name == '':
            name = input('Введите название фильма\n(для выхода впишите -1)')
            nearest = []
            if name == '-1':
                comand = 0
                continue
            for i in theatrList:
                res = i.get_nearest(i, name)
                if res[0] != -1:
                    if nearest[0] > res[0]:
                        nearest = [res, i]
        if len(nearest) != 0:
            flagCommand = \
                f'Ближайший сеанс в кинотеатре {nearest[1].name} \n Дата показа: {nearest[0][0].strftime("%Y-%m-%d %H:%M")}'
            if int(input('Купить билет? (1 - да, 0 - нет)')):
                theatrList[theatrList.index(nearest[1])].zalList[theatrList[theatrList.index(nearest[1])].zalList.index(nearest[0][1])].print_map()
                try:
                    x = int(input())
                    y = int(input())
                except ValueError:
                    flagCommand = '! Ошибка, вводите только цифры. Повторите попытку'
                theatrList[theatrList.index(nearest[1])].zalList[theatrList[theatrList.index(nearest[1])].zalList.index(nearest[0][1])].buy()
                name = ''
        else:
            flagCommand = 'В ближайшее время нет ни одного сеанса'
        comand = 0


    if comand == 3:
        name = input('Введите название фильма\n')
        dur = 0
        try:
            dur = int(input('Введите длительность фильма в минутах'))
        except ValueError:
            flagCommand = 'Длительность - одно число'
        filmList.append(Kino.seans())
        filmList[-1].name = name
        filmList[-1].duration = dur
        comand = 0

    if comand == 4:
        theatrList.append(Kinotheatr.Theatr)
        theatrList[-1].name = input('Введите название кинотеатра\n')
        print('Кинотеатр создан!')
        comand = 0