"Example Diamond problem"
'If You Want Know Resolution Method Order You Only Add "help(object)"  '
class A: 
    def show2(self):
        self.string = 'class B'
        # self.jumlah = len(self.string)
        return self.string
        
class B(A):
    def show3(self):
        self.string = super().show2()
        self.jumlah = len(self.string)
        print('|'*self.jumlah)
class C(B):
    
    def show1(self):
        self.string = super().show2()
        self.jumlah = len(self.string)
        print('|'*self.jumlah)
        print(self.string)
class D(C):
    pass
E = D()
E.show1()
E.show3()


"MAGIC METHOD"
class A:
    def __init__(self,name,karakter,score):
        self.name = name
        self.karakter = karakter
        self.score = score
    def __repr__(self):
        return f'~ only for Debug ~ \n {self.name} \n karakter = {self.karakter} \n score = {self.score}'
    def __str__(self):
        return f'~ for output like __repr__ ~ \n {self.name} \n karakter = {self.karakter} \n score = {self.score}'
    def __add__(self,objek):
        self.Total =  self.score + objek.score
        return f'\n Total score = {self.Total}'
   
B = A('Fanny','PMS',50)
C = A('Ega','Cuek',90)
# not output method __repr__ because this method only for debug not for output normal
print(B)
# if want output method __repr__ you must add repr(object)
print('\n')
print(C)
print(B + C)

