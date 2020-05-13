class Hero:
    # private class variable
    __jumlah = 0
    def __init__(self,name,health,attpower,armor):
        self.__name = name
        self.__healthBase = health
        self.__attpowerBase = attpower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attpower = self.__attpowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax
        Hero.__jumlah += 1
    @classmethod
    def jumlah(cls):
        return f'Jumlah Hero -> {cls.__jumlah}'
    @property
    def gainExp(self):
        pass
    @gainExp.setter
    def gainExp(self,expValue):
        self.__exp += expValue
        if self.__exp >= 100:
            print(f'{self.__name} LEVEL UP')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attpower = self.__attpowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
    @property
    def info(self):
        self.gainExp = 200
        info = f'{self.__name} Level {self.__level}: \
            \n\t Health: {self.__healthBase}/{self.__healthMax} \
            \n\t Attack Power: {self.__attpower}\
            \n\t Armor: {self.__armor} '
        return info
Tiny = Hero('Tiny',100,10,5)
Axe = Hero('Axe',100,2,20)
print(Hero.jumlah())
print(Tiny.info)
print(Axe.info)
