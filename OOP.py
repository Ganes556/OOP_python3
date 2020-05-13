# from time import sleep
# import random
# import sys

# # class Hero:
# #     def __init__(self,name,health,attackPower,armor):
# #         self.__name = name
# #         self.__health = health
# #         self.__attPower = attackPower
# #         self.__armor = armor
# #     # getter
# #     def getName(self):
# #         return self.__name
# #     def getHealth(self):
# #         return self.__health
# #     def getArmor(self):
# #         return self.__armor
# #     # setter
# #     def diserang(self,lawan):
# #         self.__health -= lawan.__attPower-self.__armor
        
# # kenji = Hero("kenji",200,10,5)
# # zymeth = Hero("zymeth",100,20,2)
# # kenji.diserang(zymeth)
# # print(kenji.getHealth())
# # print(kenji.getName())
# def mengetik(s):
#     while True:
#         for c in s + "\n":
#             sys.stdout.write(c)
#             sys.stdout.flush()
#             sleep(random.random() * 0.1)
    
# kalimat = "keren sekali"
# mengetik(kalimat)

# nilai assert berguna untuk cek data yang salah
# a = [1,2,3,4,5]
# for i in a:
#     b = 5
#     assert i != b
#     print("salah")

# contoh lainnya menggunakan assert
def multiple(x,y):
    assert y !=0
    print("perkalian tidak boleh menggunakan 0")
    return x*y

a = multiple(10,1)
print(a)