#String
""" String ifadeler bir dizidir (sequence). Belli alt parçacıkların bir araya gelmesi ile oluşur.
    Örneğin; 'e','n','e','s' karakterlerinin bir araya gelmesi ile karakter dizisi olan
    string meydana gelir. Listeler gibi indislerden oluşur.

"""
variable = "Hello WORLD"

#String İndisleme
variable2 = variable[5] # variable değişkeninin 5. indisini erişip variable2 değişkenine atıyoruz. -1 ile
                        # son string elemanına ulaşabiliyoruz.

#String Slice (Dilimlemek)
""" Belli bir karakter indis aralığını almamızı sağlar."""
variable3 = variable[2:5] #variable değişkeninin 2,3,4 indis karakterlerini alır.

#String Değişebilirlik (Mutability)
""" String veri tipinin her bir indis karakteri değiştirilemiyor. Değişebilirlik özelliği yoktur. Ekleme özelliği de
    yoktur ancak birleşme (concate) özelliği vardır. İstenilen indis değerini değiştirmek için de slice yöntemi ile istenilen
    karakter aralığı alınır ve yeni bir değişkende yeni indis ve istenilen karakter aralığı birleştirilir. (concatenation)"""

#greeting = "Hello, world!"
#greeting[0] = 'J'            # ERROR!
#print(greeting)

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)  


#String Metotları
""" count(): bir string değerin içinde belirtilen karakterden kaç adet olduğunu söyler.
    find(): Aranan değerin kaçıncı indisten itibaren başladığını söyler. Yoksa -1 döndürür.
    len(): Stringin toplam karakter sayısını verir.
    split(): Stringi bölmemize yardımcı olur. Liste geriye döndürür.
    join(): Verilen bir listeyi birleştirerek stringe çevirir. Birleştirme sırasında aralara karakter koyabiliyoruz.
    strip(): Başta veya sondaki boşluk ve yeni satır ('\n') karakterini siler.
    replace(): Verilen iki değeri birbiriyle yer değiştirir.
    lower(): Tüm karakterleri küçük harfe çevirir.
    upper(): Tüm karakterleri büyük harfe çevirir.
    index(): İçerisine girilen karakterin indis numarasını verir.
    """
cumle = "Python ogreniyorum. Haydi sizde ogrenin. Bunu başarabileceğinize inanıyorum"
duyuru = "Özverili olun"

print(cumle.count("og"))
print(cumle.count("n"))
print(cumle.find("ogre"))
print(len(cumle))
print(cumle.split("."))
print(cumle.split(" "))
liste = cumle.split(".")
print(":".join(["nes","pos","tos"])) # "nes:pos:tos"
print(liste[0])
print(duyuru.replace("Özverili","Dirayetli"))
print(duyuru)
print(duyuru.lower())
print(duyuru.upper())

# String Birleştirme (Concatenate) ve Multiply
""" Stringleri toplayabiliriz (birleştirme işlemi yapar) ve çarpabiliriz (tekrarlama işlemi yapar). """
word = "drink"
word2 = "milk"
word3 = word + " " + word2
print(word3)
print(word3 * 3)



#String Biçimlendirme
""" Konsol uygulamalarında ya da diğer ekran uygulamalarında bir yazı bastırmak çok
    önemlidir. Bazen bu yazıların içinde dinamik değişkenlerin değerinide 
    yazdırmamız gerekiyor. İşte bu noktada string biçimlendirme yöntemlerini bilmemiz
    gerekiyor. Bu yazımızda bundan bahsedeceğiz."""

number = 18
name = "tarık"
sale = 89.988888

#format ile String Biçimlendirme
print("en sevidğim sayı {}'dir.".format(number))
print("{isim} adlı kullanıcı {yas} yaşındadır.".format(yas=number,isim=name))
print("Birinci değer : {0}, İkinci değer : {1}".format(number,name))
print("Birinci değer : {1}, İkinci değer : {0}".format(number,name))
v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))

#% ile String Biçimlendirme
print("Benim adım %s" % name)
""" string %s
    integer %d
    float %f """
print("Telefonun ücreti : %.2f ₺'dir" % sale)

#+ ile String Biçimlendirme
""" Burada dikkat edilmesi gerken kural, değişkenler string olmalıdır."""
print("Adım "+ name + ", yaşım " + str(number) + "!!!")

#, ile String Biçimlendirme
print("Adım ", name,", yaşım ",number,"!!!")