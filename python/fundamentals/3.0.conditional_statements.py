""" 
    Koşul ifadeleri gündelik hayatımızda da karşımıza çıkmaktadır. Bu doğru mu, bu böyle
    miydi, 17 2'ye tam bölünür mü? gibi soruların bir karşılığı vardır ve bu sorunun sahibi buna
    göre bir olayı gerçekleştirecek olabilir. İşte python daki koşul yapısı da bu
    gibi durumlar karşımızı çıkınca sorunun cevabına göre işlemler yapmamızı sağlıyor.
    Koşul ifadesi diye adlandırdığımız ifade if - else ifadesidir. Koşul ifadesi doğruysa bunu
    yap, yanlışsa bunu yap dememizi sağlamaktadır. Yapı bool değerler ile çalışır. Bu yüzden if
    yapısına bool değer döndürecek koşullar yazmamız önemli bir kuraldır.

    if BOOLEAN EXPRESSION:
        STATEMENTS_1        # Eğer koşul True ise burayı çalıştır
    else:
        STATEMENTS_2        # Eğer koşul False ise burayı çalıştır
    
    Not: Eğer bir koşulun olumsuz durumunda bir olay gerçekleştirmek istemiyorsanız else yapısını
    kullanmayabilirsiniz (Unary selection).
"""


#if - else Yapısı
x = 15
y = 10

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")


# İç içe Koşul Yapısı (Nested Conditioanl)
""" Sorgulamasını yaptığınız koşulun 2'den fazla sonucu olabilir. İşte bu durumda iç içe koşul yapısını kullanabilirsiniz.
    Örneğin.: x ve y adında iki değişkenin karşılaştırmasını yaparsanız; x y'den büyük olabilir, y x'denn büyük olabilir ve x y birbirine
    eşit olabilir. Üç tane koşul ortaya çıktı tamda burada iç içe koşul yapısını kullanabiliriz. Gelin koduna bakalım."""

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")


# Zincirleme Koşul Yapısı (Chain Conditioanl)
""" Evet iç içe döngülerle uğraşmak biraz kafa karıştırıcı ama imdadımıza python yetişiyor. Python bu karışıklığı önlemek amacıyla 'elif' denen
    bir yapı sunuyor. Bu yapı bir if yapısı tanımlandıktan sonra tanımlanabilen ve if yapısı gibi bool değer döndüren bir ifadeye ihtiyaç duyar.
    Gelin x y karşılaştırma örneğimizi elif yapısıyla gerçekleştirelim.
    
    Not: elif yapısı birden fazla kullanılabilir. İstenirse else yapısı kullanılmayabilir."""

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")


#if - else örneği
""" Not ortalamasına göre takdir teşekkür alıp alamadığını söyleyen program 
    Not: input() fonksiyonu ile kullanıcıdan veri alırız. Fonksiyon geriye string değer
    döndürür. İçeriğe göre dönüşümler yapabilirsiniz."""

ders1 = int(input("1. ders notunuz : "))
ders1_saat = int(input("1. ders saati : "))
ders2 = int(input("2. ders notunuz : "))
ders2_saat = int(input("2. ders saati : "))

ort = (ders1 * ders1_saat + ders2 * ders2_saat) / (ders1_saat + ders2_saat)

if ort >=85 and ort <= 100:
    print("Takdir belgesi almaya hak kazandınız.")
elif ort >=70 and ort <= 84:
    print("Teşekkür belgesi almaya hak kazandınız.")
elif ort >= 50 and ort <= 69:
   print("Sınıfı normal geçtiniz.")
else:
    print("Sınıfta kaldınız.")

""" Karakter dizisinde 'a', 'e', 'i', 'o', 'u' harflerinin kaç tane oluğunu hesaplayan program"""
s = "Acele ile menzil alınmaz"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)