from bin import Zal


class Theatr:
    def __init__(self):
        self.name = ''
        self.zalList = []

    def get_nearest(self, name):
        seans_time_list = []
        for i in zalList:
            seans_time_list.append((i.get_nearest(name, i), i))
        seans_time_list = list(sorted(seans_time_list))
        if len(seans_time_list) != 0:
            return seans_time_list[0]
        return -1

    def add_zal(self, path):
        zalList.append(Zal.zal())
        zalList[-1].get_map(path)