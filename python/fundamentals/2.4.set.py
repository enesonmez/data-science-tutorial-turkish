""" 
    Kümeler veri tipi matematiksel kümelerde yaptığımız işlemlerin aynısını yapmamıza
    olanak sağlar. (kesişim kümesi bulma, birleşim kümesini bulma,vb.) 
    Aynı elemandan iki tane olamaz. Aynı yazsanız dahi tek bir tane sayılır.
    Not: İçerisindeki veriler değişemez ama eleman eklenebilir. Bu yüzden değişebilen 
    veri tipleri eleman olarak eklenemez. (liste,sözlük,kümelist(): Boş liste oluşturur 
    veya string bir değeri karakter karakter listeye çevirir.
    Aynı zamanda diğer koleksiyon tiplerini listeye çeviriyor.)
"""

kume = {1,2,3,3}
empty_set = set()

print(kume)
print(len(kume))


#Küme Metodları
""" 
    add(): Yeni eleman ekler.
    update(): Birden fazla eleman eklememizi sağlar.
    remove(): İstenilen elemanı siler.
    discard(): Remove ile aynı işi yapar ancak olmayan bir elemanı silmeye kalktığımızda hata vermez.
    pop(): Eleman siler.
    intersection(): Kesişim kümesi bulur.
    difference(): Fark kümesi bulur.
"""

arabalar = {"BMW","Mercedes","Audio","Toyota"}
print(arabalar)

arabalar.add("Renault")
print(arabalar)
arabalar.update({"Opel","Hyundai"})
print(arabalar)
arabalar.remove("Hyundai")
print(arabalar)
arabalar.pop()
print(arabalar)

gozlukluler = {"Tarık","Kadir","Meltem","Zehra"}
erkekler = {"Tarık","Kadir","Mustafa","Celil"}
kadinlar = {"Selin","Meltem","Gizem","Kadriye","Selin"}


#Kesişim Kümesi
print(gozlukluler & erkekler)
kesisim = gozlukluler.intersection(erkekler)
print(kesisim)


#Kümenin Birleşimi
erkekler_kadinlar = erkekler | kadinlar
print(erkekler_kadinlar)


#Fark Kümesi Bulma
gozluklu_fark_erkek = gozlukluler - erkekler
erkekler_fark_gozlukluler = erkekler - gozlukluler
print(gozluklu_fark_erkek)
print(erkekler_fark_gozlukluler)
fark = erkekler.difference(gozlukluler)
print(fark)

liste = [1,2,3,4,5]
demet = (1,2,3,4,5)
sozluk = {1:120,2:121,3:122}


#Koleksiyon Veri Tiplerini Kümeye Dönüştürme
print(set(liste))
print(set(demet))
print(set(sozluk))