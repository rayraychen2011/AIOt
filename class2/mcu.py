class gpio:
    def __init__(self):
        self.D0 = 16
        self.D1 = 5
        self.D2 = 4
        self.D3 = 0
        self.D4 = 2
        self.D5 = 14
        self.D6 = 12
        self.D7 = 13
        self.D8 = 15
        self._SD3 = 10
        self._SD2 = 9

    @property
    def D0(self):
        return self.D0

    @property
    def D1(self):
        return self.D1

    @property
    def D2(self):
        return self.D2

    @property
    def D3(self):
        return self.D3

    @property
    def D4(self):
        return self.D4

    @property
    def D5(self):
        return self.D5

    @property
    def D6(self):
        return self.D6

    @property
    def D7(self):
        return self.D7

    @property
    def D8(self):
        return self.D8

    @property
    def SD3(self):
        return self._SD3

    @property
    def SD2(self):
        return self._SD2
