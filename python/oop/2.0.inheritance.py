""" 
    Sınıfların birbirinden türemesi diyebiliriz. Birbiriyle ortak nitelikleri
    bulunan iki sınıf biri base class diğeri sub(child) class olarak birbirine 
    kalıtılabilir. Bu sayede fazladan kod yazımından kaçınmış oluruz. Bu kalıtımı
    biyolojideki kalıtım konusuna benzetebiliriz. Babanın genleri çocuğa aktarılır.
    Çocuk babadan kalıtım almış olur. oop deki kalıtımda böyledir.
"""


class Hayvan(): #base class
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def bilgi(self):
        print("Benim adım ",self.isim," ben bir hayvanım!!!")

    def whoIsIt(self):
        print("Ben hayvanım.")


class Kopek(Hayvan): #sub(child) class
    def __init__(self,isim,yas,tur):
        super().__init__(isim,yas)
        self.tur = tur
    
    def kopekBilgi(self):
        print("Benim adım ",self.isim,", yaşım ",self.yas,", türüm ise ",self.tur," ben bir köpeğim!!!")

    # override
    def whoIsIt(self):
        print("Ben kediyim.")


nesne = Kopek("pati",3,"gold")
nesne.bilgi()
nesne.kopekBilgi()

""" 
    sub class ta tanımlanan super() fonkisyonu base classımızı temsil eder.
    Türetilmiş sınıf çalıştığı an base class ta çalışır. Bu yüzden super
    fonksiyonu ile base class ın init fonksiyonuna değişkenleri yolluyoruz.
"""