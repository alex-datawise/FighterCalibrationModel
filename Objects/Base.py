class RestrictedRange:
    def __init__(self, range_min, range_max):
        self.__range_min = range_min
        self.__range_max = range_max
        self.__min = 0
        self.__max = 0

    def __repr__(self):
        pass

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, value):
        if value < self.__range_min:
            value = self.__range_min
        self.__min = value

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, value):
        if value > self.__range_max:
            value = self.__range_max
        self.__max = value

    def range(self):
        return [self.__range_min, self.__range_max]
