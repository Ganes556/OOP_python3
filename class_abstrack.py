from abc import ABC, abstractclassmethod
# class Makanan(ABC):
#     @abstractclassmethod
#     def makanan_pokok(self):
#         print('ini abstrack')
# class Dimakan(Makanan):
#     def makanan_pokok(self):
#         print("ini method in abtrack")
#     def lauk(self):
#         print("ini objek lauk")
# Ayam = Dimakan()
# Ayam.lauk()
class Button(ABC):
    def __init__(self,website2):
        self.website2 = website2
    @abstractclassmethod
    def click(self):
        pass
    @property
    @abstractclassmethod
    def website2(self):
        pass
class push_button(Button):
    def click(self):
         print(f'Go To: {self.website2}')
    @Button.website2.setter
    def website2(self,input):
        self.__website = input
    
    # getter decorator berisi return 
    @website2.getter
    def website2(self):
        return self.__website
tombol = push_button('wikipedia.com')
tombol.click()