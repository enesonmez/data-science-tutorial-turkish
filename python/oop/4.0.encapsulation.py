""" 
    Sınıfları tanımlarken içerisinde birçok değişken ve metod bulunacak şekilde
    tanımlıyoruz. Ancak bazı değişkenlerin ve metodların dışarıdan erişilmemesi
    gerekebilir. Bu gibi durumlarda kapsülleme yapıyoruz ve değişkenlerin gizliliğini
    sağlıyoruz. Yani bir nevi dışarıdan bilgi saklamış oluyoruz. Bu durum yazdığımız
    kodun güvenliğini sağlamış oluyor. Ya da bug'a düşmemesini sağlıyor.
    Bilgi saklama erişim belirteçleri (public, private, protected) ile gerçekleştirilir.
    public : herkesin kullanabileceği özellik ve davranışlardır.
    private : sadece sınıf içinde kullanılabilen özellikler ve davranışlardır.
    protected : sınıf içinde ve miras alınan alt sınıflarda kullanılır.
"""

class Chat():
    def __init__(self,isim,soyad,mesaj):
        self.isim = isim
        self.soyad = soyad
        self.__mesaj = mesaj #private etmiş olduk sadece sınıf içinden ulaşabiliyoruz.

    def getMesaj(self):
        return self.__mesaj
    
    def setMesaj(self,mesaj):
        self.__mesaj = mesaj
    
    def __userDrop(self): # metod private edildi. Sadce sınıf içinden kullanılabilir.
        print("kullanıcı silindi.")


c1 = Chat("Metin","Kırkpınar","telefon şifrem 542198")

print(c1.getMesaj())
c1.setMesaj("Değişken kapsüllendi :)")
print(c1.getMesaj())

