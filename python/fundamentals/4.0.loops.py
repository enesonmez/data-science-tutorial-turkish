""" Tüm programların temel yapı taşı, bazı kodları defalarca tekrarlayabilmektir. 
    İster her gece milyonlarca müşterinin banka bakiyesini güncelliyor olsun, ister binlerce 
    kişiye e-posta mesajı göndermek olsun, programlama, bilgisayara birçok tekrarlı işlem yapma 
    talimatı vermeyi içerir. Hesaplamada, bu tekrarlayan yürütmeyi yineleme olarak adlandırıyoruz. 
    Bir işlemin belli bir miktar ya da sürekli tekrar etmesi işlemini yazılım dünyasında
    döngüler sağlar. Örneğin ekrana 10 tane yıldız işlemi yazdırmak için teker teker
    print edebiliriz ya da tek bir print ve döngü ile ekrana yazdırabiliriz. Listelerin 
    tüm elemanlarına döngü yardımıyla ulaşabiliriz.

    Python'da döngüler (loop) for ve while olmak üzere ikiye ayrılır.
"""

#for döngüsü
""" Başlangıç ve bitiş aralığı olan döngülerdir. Bu şekilde olan döngülerde kullanılabilir.
    Listelerde, tuplelarda, stringlerde kullanılabilir.
    For döngüsünde yinelenen liste, string, tuple gibi veri tiplerine iterator (iterable) denir. Bu 
    veri tiplerinin her bir elemanının atıldığı değişkene ise iterator variable veya loop variable 
    denir."""
sayilar = [1,2,3,4,5,6,7,8,9]

#Liste ile for döngüsü
""" Liste elemanlarını teker teker geçici elemana atar ve listedeki eleman bitene kadar devam eder."""
for sayi in sayilar:
    print(sayi)

#Range fonksiyonu ile for döngüsü
""" Range fonksiyonu belli bir aralıkta liste oluşturur. Liste mantığı ile döngü oluşturur."""
for sayi in range(1,10,2):
    print(sayi, end='-')

#For döngüsü ile ilgili Örnekler
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")

#for döngüsü ile çift sayı örneği
cift = []
for sayi in range(1,100):
    if sayi%2==0:
        cift.append(sayi)
print("\nÇift sayilar : " + str(cift))

#for döngüsü ile filtrelenmiş kelimeler örneği
"""4 karakterli kelimeleri bulacak ve ilk harfi büyük olacak şekilde yeni listeye atayacak."""
kelimeler = ["uçak","gemi","portakal","ananas","iskemle"]
filtrelenmis_kelimeler = []

for kelime in kelimeler:
    if len(kelime) == 4:
        filtrelenmis_kelimeler.append(kelime.title())
print("For Döngüsü ile Filtrelenmiş kelimeler : " + str(filtrelenmis_kelimeler))


#While döngüsü
""" Şart sağlandığı müddetçe çalışan döngülerdir. """

#while döngüsü ile filtrelenmiş kelimeler örneği
count = 0
filtre_word = []
while count != len(kelimeler):
    if len(kelimeler[count]) == 4:
        filtre_word.append(kelimeler[count].title())
    count+=1
print("While Döngüsü ile Filtrelenmiş kelimeler : " + str(filtre_word))

#break ve continue
""" break ingilizce kırmak anlamına gelir bizde döngüleri kırmak amacıyla kullancağız.
    continue ise devam et anlamına gelir yazılım dünyasında ise continue kullanılan 
    satırdan sonraki satırları atlar ve döngünün başına gelir ve döngüye devam eder. """

for number in range(1,10):
    if number == 3:
        print("sayı atlandı.("+str(number)+")")
        continue
    print(number)
    if number == 8:
        print("döngü kırıldı.("+str(number)+")")
        break

#enumerate fonksiyonu
""" Bazen bir listedeki elemanlerın liste sırasına ihtiyaç duyarız işte bu noktada 
    enumerate yardımımıza yetişir ve bize istediğimizi verir. bu fonkisyon obje return 
    eder ve liste elemanı ve indisini bir demette tutar. """

aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
print(list(enumerate(aylar)))

for indis,ay in enumerate(aylar):
    print("{} indisindeki ay : {}".format(indis,ay))
        