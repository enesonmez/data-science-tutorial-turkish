""" 
    Çok biçimlilik, kalıtılmış sınıflar içerisinde bulunan aynı isimdeki
    metotların farklı işlevler uygulamasına polymorphism denir.
    Çok biçimlilik olabilmesi için birden fazla sınıfın kalıtılmış olması lazım.
    Parent classındaki metodu child class'larında da oluşturup
    farklı sonuçlar döndürmesi diye özetleyebiliriz.
"""

class Hayvan(): #base class
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def bilgi(self):
        return "Benim adım {} ben bir hayvanım!!!".format(self.isim)


class Kopek(Hayvan): #sub(child) class
    def __init__(self,isim,yas,tur):
        super().__init__(isim,yas)
        self.tur = tur
    
    # override
    def bilgi(self): 
        return "Benim adım {}, yaşım {}, türüm ise {}; ben bir köpeğim!!!".format(self.isim,self.yas,self.tur)

    def __str__(self):
        return "Bu bir köpektir!!!"


class Kedi(Hayvan): #sub(child) class
    def __init__(self,isim,yas,tur):
        super().__init__(isim,yas)
        self.tur = tur
    
    # override
    def bilgi(self): 
        return "Benim adım {}, yaşım {}, türüm ise {}; ben bir kediyim!!!".format(self.isim,self.yas,self.tur)


# polymorphism - UpCasting
k1 = Hayvan("boncuk",1)
k2 = Kopek("karabaş",6,"çoban köpeği")
k3 = Kedi("kül",2,"van kedisi")

hayvan_listesi = [k1,k2,k3]
for hayvan in hayvan_listesi:
    print(hayvan.bilgi())


def bilgiGoster(hayvan:Hayvan):
    print(hayvan.bilgi())

bilgiGoster(k1)
bilgiGoster(k2)
bilgiGoster(k3)

# __str__ metodu
""" 
    Bu metodun kullanılma amacı nesne print ile direk bastırıldığında ekranda
    teknik sayılabilecek bir yazının çıkması yerine daha anlaşılabilir bir yazı
    çıkarmak için kullanılır.
"""

print(k2)

