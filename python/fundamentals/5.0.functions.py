""" Fonksiyon, belli bir işi yapan parçalar olarak ifade edilebilir. Yazılım dünyasında bir
    işi yapan kod blokları bir bütün halinde yazılmaz bunu parçalara bölerek yani fonksiyonlara
    bölerek işi gerçekleştiririz. Parçaları birleştirerek bir bütün elde ederiz.
    Şuana kadar birçok kod yazdık ancak hiç fonksiyon yazmadık. Ancak yazılan hazır fonksiyonları
    kullandık. Örneğin print, input, len, vb. 
    Fonksiyonları kullanmamızın en büyük nedeni kod tekrarından kaçınmaktır. Bir projede birden
    fazla yerde mod alma işlemi kullanıyorsak bunu her satırda yazmak yerine bir fonksiyon
    yazıp bunu ilgili satırlarda kullanmak temiz bir kod yazmanızı sağlayacak.
    Not: Fonksiyonların çalışması için fonksiyonu çağırmamız lazım. """

#Fonksiyon Tanımlama
""" Fonksiyon tanımlamak için definition (tanım) kelimesinin ilk üç harfini kullanarak bir fonksiyon 
    tanımlayacağımızı belirtiriz. Sonrasında fonksiyon ismini yazıp parantez açıp kapatırız ve iki nokta
    koyarak aşağı geçeriz. Fonksiyona yazmak istediğimiz kod bloklarını 4 boşluk karakteri bırakarak 
    girintili yazmamız gerekmektedir. Döngülerde, koşul ifadelerinde olduğu gibi.
    Not: Yazılan fonksiyonun çalışması için fonksiyon çağrısı (call, invocation) yapmamız gerekmektedir.
    Not: Fonksiyon isimlerini seçerken python keyword'ü olmamaına dikkat etmelisiniz.
"""
def firstFunction():
    print("İlk fonksiyonumu tanımladım.")

firstFunction()

#Fonksiyonlarda Parametre Tanımlama
""" Fonksiyonlar insanlar gibi bazı işleri yapmadan önce dışardan veri alma ihtiyacı duyabilir.
    Bizde böyle fonksiyonlar yazdığımız zaman fonkssiyonumuza değer göndermemiz lazım.
    Örneğin iki sayıyı toplayan fonksiyon yazdığımızda iki sayıya ihtiyaç duyarız işte bu iki
    sayıyı fonksiyonumuza dışardan veri olarak göndeririz. 
    Not: Fonksiyonun aldığı değerlere parametre, fonksiyona gönderilen değerler ise 
    argüman denir. """

def topla(num1,num2):
    print(num1 + num2)
topla(10,20)

""" Eğer parametre alan fonksiyonları çağırırken argüman yollamazsak derleyici hata verir.
    Bunu engellemek için parametrelere varsayılan değer verebiliriz. Bu sayede argüman
    yollamasak ya da eksik yollasak dahi fonksiyon varsayılan değerler üzerinden işlemlerini 
    gerçekleştirecek. """

def topla2(num1 = 0,num2 = 0):
    print(num1 + num2)
topla2()

#Anahtar Kelimeli (Hedefli) Argüman Yollama
""" Şuana kadar yaptığımız fonksiyon örneklerinde pozisyonel argüman mantığı kullandık.
    Yani her verdiğimiz argüman parametrelere sırası ile yerleşti. Şimdi size anahtar kelimeli
    (hedefli) argüman mantığını anlatacağım. Anahtar kelimeli argüman, değerleri sırası ile değil
    parametreleri hedef alarak yollamak diyebiliriz. Yani argüman yollarken odak noktamız
    parametredir. """

def hedef(parametre1,parametre2,parametre3):
    print("1. parametre : {}, 2. parametre : {}, 3. parametre : {}".format(parametre1,parametre2,parametre3))
hedef(parametre2 = 10, parametre3 = 122, parametre1=87)

#Fonksiyonlarda return kullanımı
""" İnsanlar belli bir olayı değerlendirir ve bunun sonucunda dışarıya sözlü veya yazılı
    olarak çıktı (dönüt) verir. Fonksiyonlarda içerisinde yapılan işlemler sonrasında dışarıya
    çıktı vermesi gerekebilir. Bu noktada return yapısını kullanırız ve dışarıya değer
    göndeririz. Bu dönen değeri programımızın içinde de kullanabiliriz. 
    Return ifadesi kullanıldığı anda fonksiyon çağrısı sonlandırılır ve geriye değer döndürür.
    İster bir koşul yapısı içinde kullanın ister bir döngü içinde kullanın yorumlayıcı fonksiyonda return ifadesini
    gördüğü an fonskiyon çağrısını durdurur."""

def topla3(num1 = 0, num2 = 0):
    return num1 + num2
print(topla3(5,5))

#Fonksiyon Örnekleri
""" Tek çift sayı tespit eden fonksiyon """
def tekCift(num = None):
    if num:
        print("Çift" if num % 2 == 0 else "Tek")
    else:
        print("Değer girilmedi.")
tekCift(6)

""" Küçük harften büyük harfe çeviren fonksyon """
def buyut(yazi=None):
    cıktı = ""
    if yazi:
        for harf in yazi:
            if ord(harf) >= 97 and ord(harf) <= 122:
                cıktı += chr(ord(harf) - 32)
            else:
                cıktı += harf
        return cıktı
    else:
        return "değer giriniz"
print(buyut("KaMiL"))


#Karadelik (Çoklu) Kapasiteli Parametre
""" Fonksiyonlara tek parametre ile birden fazla argüman yollayabiliriz. Bu tür fonksiyonlara
    karadelik kapasiteli fonksiyon denir. Pozisyonel argüman çağrımı yapıldığında tek yıldız
    kullanılır ve değerleri demet içinde tutar. Anahtar kelimeli argüman çağrımında ise
    iki yıldız kullanırız ve değerleri sözlük içinde tutar. 
    Not: Bu iki yolu aynı anda kullanabiliriz."""

def function(*args):#pozisyonel argüman kullanımı
    print(args)
function("enes",12,12.2,True)

def fonksiyon(**kwargs):#anahtar kelimeli (keyword) argüman kullanımı
    print(kwargs)
    print(kwargs["isim"])
    for key,value in kwargs.items():
        print("Anahtar : {}, Değer : {}".format(key,value))
fonksiyon(isim="Mahmut", soyad="Tuncer", yas=50)

#lambda (anonim) Fonksiyonlar
""" Bazen hız kazanmak için küçük işler yapan fonksiyonları lambda denen tek satırlık
    fonksiyonlar ile gerçekleştiririz. Örnekleri aşağıdadır. """

toplama = lambda sayi1,sayi2: sayi1 + sayi2
ussu = lambda taban,us: taban**us
print(toplama(10,85))
print(ussu(5,4))


""" Bir fonksiyon yazmadan önce kendinize sormanız gereken sorular?
    1) Fonksiyon ne iş yapacak?
    2) Kaç parametre tanımlamalıyım?
    3) Parametrelerin veri türleri ne olmalı?
    4) Fonksiyonun return değerinin veri türü ne olmalı?
"""

""" Fonksiyon içinde başka bir fonksiyon çağrısı yapabilirsiniz.
    Fonksiyon içinde liste ve sözlük değerlerini değiştirmek side effect (yan etki)
    olarak adlandırılır. Fonksiyona parametre tanımlamasını genellikle by-value yöntemi ile
    gerçekleştiririz. Bu yöntem bellekte yeni bir local değişken yaratarak argüman olarak verilen
    değişkenin değerini kopyalar. Ancak parametreye verilen liste ve sözlükler by-referance yöntemi
    ile fonksiyonda kullanılır. Bu yöntem bellekte yeni bir veri tipi oluşturmaz parametre değişkeni
    verilen argümanın  bellekteki konumuna işaret eder. Hal böyle olunca fonksiyon içerisinde
    liste ve sözlükte yapılacak bir değişiklik fonskiyona verilen değişkende de değişiklipe sebebiyet verir.
    İşte bu olaya side effect diyoruz.   

    Side effect oluşturmanın başka bir yolunu ise global değişkenleri fonksiyonlarda global ifadesini
    kullanarak değişken değerinde değişiklikler yapmak olarak gösterebiliriz.
"""

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)


def double(n):
    global y
    y = 2 * n
	
y = 5
double(y)
print(y)

""" Fonksiyonlarda geriye birden fazla değer döndürebiliyoruz. Return ifadesinin yanına birden fazla
    değişkeni ya da değeri virgülle ayırıp yazarsak bu işlemi gerçekleştirebiliriz. Python birden fazla değişkeni 
    veya değeri yan yana virgülle ayrıldığını görünce bunu bir tupple veri tipine dönüştürerek return ediyor.
    Return eden değeri bir değişken oluşturup eşitleyebiliriz. Bunu yaparsak değişkenin veri tipi tuple olur. Eğer
    return eden değer adedi kadar değişken oluşturup eşitlersek her değişken eşitlendiği değerin veri tipine sahip olur.
    Değişkenlere değerler fonksiyondan return edilen sırada atanır.
"""

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

circumference, area = circleInfo(10)


""" Bir fonksiyona tuple veri tipindeki değişkeni argüman değer olarak yollamak isterseniz aşağıdaki kod
    bloğunu inceleyin.
    * karakteri ile tuple'ın içindeki değerleri fonksiyon parametrelerine teker teker yollarız.
"""

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z))
