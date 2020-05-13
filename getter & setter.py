class Hero:

    def __init__(self,name,power,armor):
        self.name = name
        self.__power = power
        self.__armor = armor
    @property 
    def info(self):
        info = f"Name : {self.name} \n\t Power : {self.__power} \n\t Armor : {self.armor}"
        return info
    # membuat gatter. @namaMathod.getter
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input
        return self.__armor
    @armor.deleter
    def power(self):
        print('armor dihapus')
        self.__power = None
       
   
axe = Hero("Axe",50,100)
print("memanggil -> property awal info")
print(axe.info)

print("merubah -> property info dengan menggunakan getter dan setter")
axe.name = "Doom"
axe.armor = 10
print(axe.info)
del axe.power
print(axe.__dict__)