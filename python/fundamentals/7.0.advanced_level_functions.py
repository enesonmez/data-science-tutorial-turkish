####filter fonksiyonu####
""" Bu fonksiyon isminden de anlaşılacağı üzere filtreleme işlemi yapıyor.
    Bu işi yaparken bizden işi yapacağı fonksiyonu (true veya false değer döndüren
    bir fonksiyon yazıyoruz örnekte göreceksiniz) ve veri setini istiyor.
    Bu sayede istenilen bilgiyi hızlı bir şekilde filtreleyerek bize geri
    döndürüyor. Kontrol işlemleri için kullanılır."""

liste = range(0,20)

#çift sayılar
def evenNumbers(liste):
    if liste % 2 == 0:
        return True
    else:
        return False
even = filter(evenNumbers,liste)
print("Filter ile çift sayılar : ",list(even))

#isim uzunluk kontrolü
def nameControl(names):
    return len(names)>4 and len(names)<8

names = ["enes","tarık","celalettin","gamze","kübra","mehmet","sinan","zülal","ali"]
control = filter(nameControl,names)
print("Filter ile uzunluk kontrol : ",list(control))

#tek sayılar (kısa yol)
oddNumbers = filter(lambda numbers: numbers % 2 != 0,liste)
print("Filter ile tek sayılar : ",list(oddNumbers),"\n")

####list comprehension (akıllı listeler)####
""" Döngüler yardımı ile bir listenin içini dolaşıp değerlerini bir başka listeye 
    atmak oldukça uzun bir iş ancak bunu tek bir satırda yapmamızı sağlayan
    bir yapı var. Bu yapıya list comprehension (akıllı listeler) deniyor.
    Gelin örnekle inceleyelim."""

#listdeki tüm sayıları listeleyen akıllı liste
fullNumbers = [sayi for sayi in liste]
print("List comprehension ile tüm sayılar : ",fullNumbers)
""" Başa yazılan sayi, değişkenin return ettiği anlamına gelir."""

#çift sayıları listeleyen akıllı liste
cift = [sayi for sayi in liste if sayi % 2 == 0]
print("List comprehension ile çift sayılar : ",cift)
""" Akıllı listelerde döngünün yanında koşul ifadeside kullanabiliyoruz."""

#akıllı listelerde else kullanımı
sart = [sayi if sayi % 3 == 0 else sayi*100 for sayi in liste]
print("List comprehension ile else kullanımı(3'e bolunebilme) : ",sart,"\n")

####Map fonksiyonu####
""" Filterin aksine kontrol işlemleri yerine elemanlar üzerinde
    değişiklikler için kullanılır. """

fiyat = [52,20,65,12,8,100,99,49]

def zam(liste):
    return liste + 20
zamlifiyat = map(zam,fiyat)
print("Map ile zamlı fiyatlar : ",list(zamlifiyat))

zamlifiyat2 = map(lambda zamli: zamli+20,fiyat)
print("Map ve lambda ile zamlı fiyatlar : ",list(zamlifiyat2),"\n")

####Reduce Fonksiyonu####
""" Reduce fonksiyonu map ve filter fonksiyolarının yapamadığı bir işi yapıyor.
    Bu iş ise matematiksel işlemdir. Çalışma mantığı listenin ilk iki elemanını
    alıp belirttiğimiz işlemi yapıyor ve sonucu ile listenin 3 elemanını tekrar
    işleme sokuyor ve bu işlem liste elemanı bitene kadar devam ediyor.
    Not: reduce fonksiyonunu functools kütüphanesinden ekliyoruz."""

from functools import reduce
fact = int(input("Faktöriyeli alınacak sayı : "))
sayilar = range(1,fact+1)
result = reduce(lambda num1,num2: num1*num2,sayilar)
print("Reduce ile faktöriyel : ",result)

####Any ve All Fonksiyonları####
""" Any ismindende anlaşılacağı üzere hiç mi sorusunu sorar listeye veya demete
    eğer bunların içerisinde bir tane dahi True varsa kendiside geriye True döndürür.
    Aksi takdirde False döndürür. 
    Not: Eğer listenin veya demetin içinde değişken varsa python bunu True olarak
    algılayacak ve any geriye True döndürecek. 
    Not: any sözlüktede çalışır ancak sözlüğün keylerine bakar.
    All fonksiyonu ise tüm değerlerin True olamasını ister ve sadece bu durumda
    geriye True döndürür."""

liste1 = [False,25,True]

print("Any ile : ",any(liste1))
print("All ile : ",all(liste1))
