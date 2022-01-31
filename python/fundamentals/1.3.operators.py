""" Operatörler, matematiksel işlemler, karşılaştırma (comparison) işlemleri ya da mantıksal (logic) işlemler yapmamızı sağlayan 
    ifadelerdir. Gelin bu ifadeleri birlikte görelim. """

#Matematiksel Operatörler
""" Gündelik hayatımızda çokça başvurduğumuz dört işlemler ve matematikte kullandığımız mod alma, üs alma, tam sayı bölmesi
    gibi işlemler python dilinde operatör adı verdiğimiz yapılar ile tanımlanmıştır. Böylelikle bu işlemleri kısa bir şekilde 
    halledebiliyoruz."""

value = 5 #atama operatörü
print(value + 2) #toplama operatörü 
print(value - 2) #çıkarma operatörü 
print(value * 2) #çarpma operatörü 
print(value / 2) #bölme operatörü 
print(value % 2) #mod alma operatörü
print(value ** 2) #üs alma operatörü
print(value // 2) #tam sayı şeklinde bölen operatör

#Karşılaştırma (Comparison) Operatörleri
""" İki değeri bir biri ile eşitlik, büyüklük, küçüklük gibi kıstaslar ile karşılaştırarak geriye doğru ya da yanlış olmasına
    göre bool değer döndüren operatörlerdir."""

print(1 == 2) #eşittir operatörü
print(1 != 2) #eşit değil operatörü
print(1 < 2) #küçüktür operatörü
print(1 > 2) #büyüktür operatörü
print(1 <= 1) #küçük eşit operatörü
print(2 >= 2) #büyük eşit operatörü
print(5 is 4) # eşittir operatörüne benzer ancak iki değişkenin aynı bellek bölgesini referans alıp almadığını kontrol eder.
print(5 is not 4) #eşit değil opearatörüne benzer ancak iki değişkenin aynı bellek bölgesini referans alıp almadığını kontrol eder.
#Referance Bellek Bölgesi
""" Referans bölgeleri aynı olan değişkenlerde herhangi birindeki değişim diğerine yansır. Bunu için clone'lama yapılmalıdır.
    String veri tipi değişebilir olmadığı için karışıklık yaşanmaz ancak liste veri tipi değişebilir olduğu için karışıklık
    yaşanabilir."""
a = [1,2,3]
b = [1,2,3]
print(a is b) #False değer alacak aynı değerlere sahip olmasına rağmen bellekte farklı alanlardan referans alırlar.
print(a == b) #Değer olarak baktığı için True gelir.
b = a
print(a is b) #True değer alır çünkü b'nin referans bellek böllgesini a'ya bağlamış olduk.
print(a == b) #Değer olarak baktığı için True gelir.

""" Karşılaştırma operatörleri ilkel veri tipleriyle, listelerle  ve koleksiyon metotları 
    ile de kullanabilir. """

#Mantıklsal (Logic) Operatörler
""" Mantıksal operatörler, mantık işlevi olan ve - veya - değil yapılarından esinlenerek oluşturulmuş
    yapılardır. and ve or yapıları için iki bool değer ile işlem yapılırken not için tek bir bool değer
    ile işlem yapılır. AND-OR-NOT yapılarının grafiklerini incelemenizi tavsiye ederim.

    && : ve anlamına gelir, bu durum ve bu durum doğruysa işlemi yap.
    &  : bit bazında and 'leme işlemi
    || : veya anlamına gelir bu durum veya bu durum doğruysa işlemi yap.
    |  : bit bazında or işlemi 
    and : ve anlamına gelir. && aynı anlamı taşır.
    or  : veya anlamına gelir. || aynı anlamı taşır.
    not : değerin tersini döndürür."""

print(5>0 and 5<10)
print(25%2 == 0 or 25%3 == 0)
print(not False)

#Operatörlerde Öncelik Sıralaması
""" Matematiktende aşina olacağınız konu olan işlem önceliği konusu ile benzerdir. Gelin öncelik sıralamasını
    inceleyelim:
    1.Parantez
    2.Üs alma
    3.Çarpma/Bölme/Tam Sayı Bölmesi/Mod
    4.Toplama/Çıkarma
    5.Karşılaştırma operatörleri
    6.not
    7.and/or
    
    Soru: 5*3 > 10 and 4+6==11 önceliklendirmeyi parantez kullanarak gösterirseniz aşğıdakilerden hangisi doğru olur?
    A. ((5*3) > 10) and ((4+6) == 11)
    B. (5*(3 > 10)) and (4 + (6 == 11))
    C. ((((5*3) > 10) and 4)+6) == 11
    D. ((5*3) > (10 and (4+6))) == 11"""

#in ve not in Operatörleri
""" Sequence (dizi) yapısındaki veri tipleri için kullanılan operatördür. Diziden kastımız string ve 
    collection veri tipleridir.Bu veri bunun içinde var mı sorgulaması yapar. 'not in' operatörü
    'in' operatörünün sonucunun tersini alarak kullanıcıya sunar."""

print('p' in 'apple') # String Kullanımı
print('i' in 'apple')
print('' in 'apple') # Boş küme her dizinin bir alt kümesi olduğu için True değer döndürür.
print('x' not in 'apple') # in operatörü kullanılsaydı False değer dönerdi not ifadesi ile True olarak döner.
print(9 in [3, 2, 9, 10, 9.0]) # Liste Kullanımı
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])
print("a" in ["apple", "absolutely", "application", "nope"])