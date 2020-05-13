import random
# class Tipe_ku:
#     def tipe(self,*tipe):
#         self.tipe = tipe
#         self.tipe2 = list(self.tipe)
#         self.jumlah = len(self.tipe2)
#     def show_tipe(self):
#         value = random.randrange(self.jumlah)
#         print(f'Tipe = {self.tipe2[value]}')
# class List_tipe:
#     def list_tipe(self,*list_tipe):
#         self.list_tipe = list_tipe
#         self.list_tipe2 = list(self.list_tipe)
#         self.jumlah = len(self.list_tipe2)
#     def show_list_tipe(self):
#         value = random.randrange(self.jumlah)
#         print(f'{self.list_tipe2[value]} :')
# class Pilihan_ku(Tipe_ku,List_tipe):
#     pass

# pilihan = Pilihan_ku()
# pilihan.list_tipe('Nanda','Ega','Felisa')
# pilihan.tipe('cantik','pinter','imut')
# pilihan.show_list_tipe()
# pilihan.show_tipe()
# help(pilihan)

Cewek = ['Nanda','Ega','Felissa','Dian','Lala','Sekar','Meta']
Cowok = ['Eka','Daniel','Ganes','Komang','Aris','Surya','Wira']
value_cewek = random.choice(Cewek)
value_cowok = random.choice(Cowok)
jodoh = f'{value_cowok} LOVE {value_cewek}'
print(jodoh)