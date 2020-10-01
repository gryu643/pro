
class sample():
    n1 = 0
    __n2 = 0

    def __init__(self):
        self.n1 = 100
        self.__n2 = 200

    def set_n2(self, n2):
        self.__n2 = n2

    def get_n2(self):
        return self.__n2
