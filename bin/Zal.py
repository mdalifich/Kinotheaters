from datetime import datetime, timedelta


# datetime_str = '09/19/22 13:55'


class zal:
    def __init__(self):
        self.kinoList = []
        self.map = []
        self.path = ''

    def print_map(self):
        for i in self.kinoList:
            if datatime.now == i[0]:
                self.get_map(self.path)
        for y in self.map:
            print(y, end='')

    def buy(self, x, y, kino):
        x = 2 * x
        y -= 1
        map = self.kinoList[kino][2]

        if map[y][x] == '#':
            map[y] = list(self.map[y])
            map[y][x] = 'x'
            map[y] = ''.join(self.map[y])
            print(f'Билет куплен:\n{y + 1} ряд, {x // 2} место.')
            self.kinoList[kino][2] = map

        elif map[y][x] == 'x':
            print('Место занято')
        else:
            print('Ошибка: Проверьте выбранные ряд и место и повторите попытку')

    def add_kino(self, kino, time):
        month = datatime.now.month
        year = datatime.now.year
        res = self.search_time_window(datetime.strptime(time, '%m/%d/%y %H:%M'), kino.duration)
        if res[0]:
            self.kinoList.append((datetime.strptime(time, '%m/%d/%y %H:%M'), kino, self.map))
            with open(f'{month}.{year}.docx', mode='a') as f:
                f.write(f'\n{time, kino.name, kino.duration}')
            print('Успешно')
        else:
            print(f'В это время проходит другой сеанс! Он закончится в {res[1]}')

    def get_nearest(self, name):
        self.kinoList = list(sorted(self.kinoList))
        ret = ''
        for i in self.kinoList:
            if i[1].name == name:
                ret = i[0]
        return ret

    def search_time_window(self, time_start, dur):
        result = (0, 0)
        time = datetime.strptime(time_start, '%m/%d/%y %H:%M')
        for i in self.kinoList:
            if i[0] < time < i[0] + timedelta(minutes=i[1].duration) or i[0] < time + timedelta(minutes=dur) <  i[0] + timedelta(minutes=i[1].duration):
                result = (1, i[0] + timedelta(minutes=i[1].duration))
        return result


    def get_map(self, path):
        self.path = path
        with open(path, mode='rt') as f:
            self.map = f.readlines()


