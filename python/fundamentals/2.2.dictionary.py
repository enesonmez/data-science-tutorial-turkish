""" 
    Python dilindeki kolekisyon veri tiplerinden biri olan sözlük (dictioanry) veri tipi, 
    anahtar (key) - değer (value) çiftlerini tutar.
    Gündelik hayatta kullandığımız ingilizce-türkçe
    sözlük mantığıyla aynıdır. İngilizce kelimeler key (anahtar) türkçe karşılığı ise 
    value (değer) olarak sözlük veri tipinde adlandırılır.
    Sözlüğün tüm dillerdeki karşılığı 'json' olarak söyleyebiliriz.
    Not: Sözlüklerde her key benzersizdir. Yani bir kere kullanılabilir.
    Not: Sözlükler key - value verilerini sıralı bir şekilde tutmaz. Listeler gibi sıralı bir indis mantığı yoktur.
    
    Sözlük Ne Zaman Kullanılır
    1) Bir veri parçası, tek bir öğenin bir dizi özelliğinden oluştuğunda, sözlük genellikle daha iyidir. Posta kodu 
    özelliğinin bir listede 2. dizinde olduğunu zihinsel olarak izlemeye çalışabilirsiniz, ancak kodunuzun okunması daha zor olur
    2) Bir veri çiftleri koleksiyonunuz olduğunda ve genellikle çiftlerden birini ilk değerine göre aramak zorunda kalırsanız kullanabilirisiniz.
    3) Öte yandan, birden çok çiftin aynı ilk veri öğesini paylaştığı bir veri çiftleri koleksiyonunuz olacaksa, bir sözlük tüm anahtarların birbirinden 
    farklı olmasını gerektirdiğinden sözlüğü kullanamazsınız.    
"""


#Sözlük Oluşturma
sozluk = {"word":"kelime",
            "baby":"bebek",
            "car":"araba"}

baskentler = {"Turkey":"Istanbul","England":"London","Italy":"Roma"}

karisiksozluk = {"string":"yazi","intsayi":123,"floaysayi":12.5,"liste":["eleman1","eleman2"],
                "soz":{"key1":"value1","key2":"value2"}}

empty_dict = dict()
full_dict = dict(key1="value1",key2="value2")
print(full_dict)

print(type(sozluk))


#Sözlükte Elemana Ulaşma
print(sozluk["word"])
print(len(sozluk))


#Değeri Güncelleme
print(baskentler)
baskentler["Turkey"] = "Ankara"
print(baskentler)


#Eleman Ekleme
baskentler["Japan"] = "Tokyo"
print(baskentler)


#Eleman Silme
baskentler.pop("Japan")
del baskentler["England"]
print(baskentler)


#Sözlük Metodları
""" 
    len(): Sözlükteki anahtar - değer çiftlerinin toplam sayısını verir.
    pop(): Silmek istediğimiz anahtar kelimeyi yazarak sözlükten silmemizi sağlar.
    get(): Sözlüğümüzün değerlerini getirmemizi sağlar. Sözlükte bulamazsa None değer döndürür.
    keys(): Bize sözlüğümüzdeki keyleri getirir. 
    values(): Bize sözlüğümüzdeki değerleri getirir.
    items(): Sözlükteki keyleri ve değerleri verir. Demetlere ayrılmış şekilde çıktı verir.
    popitem(): Sözlüğün son elemanını siler. 
    dict(): Boş sözlük veya dolu sözlük oluşturmamızı sağlar.
"""


print(baskentler.get("Turkey"))
print(baskentler.get("Japan","No find")) # Sözlükte yoksa istenilen değer döndürülebilir.
print(list(baskentler.keys()))
print(list(baskentler.items()))
print(list(baskentler.values()))
baskentler.popitem()
print(baskentler)


""" 
    Not: Döngü ile hem sözlük değişken adı hemde keys() metodu ile anahtarlar üzerinde dolaşabiliriz. 
    Ayrıyeten in operatörü ile sözlük değişken adı ile anahtar kelime var mı sorgulaması yapabilirsiniz.
"""
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)
for k in inventory.keys():
    print("Got key", k)

print("beard" in inventory)

