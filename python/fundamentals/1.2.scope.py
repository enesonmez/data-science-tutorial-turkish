""" Her değişkene her yerden ulaşamayız bunu da scope adı verilen terim ile
    açıklıyoruz. 
    Scope : Bir değişkenin ulaşılabilir olduğu alanları belirten bir kelimedir..
    Değişkenler local ve global olmak üzere iki şekilde tanımlanır. Python'da herbir
    değişken, fonksiyon ve class için namespace adı verilen alanlar tanımlanır. Değişkenler için tanımlanan bu 
    namespace'ler değişkene nerelerden erişilebilceğini gösterirler. Fonksiyonlarda ve sınıflarda oluşturulan değişkenler
    local değişken olarak  tutulur. Local değişkenler oluşturulduğu alan içerisinden
    erişim sağlanır. Diğer dış alandalardan erişim sağlanmaz.

    Global değişkenlere her yerden ulaşılır ve değiştirilebilir. Bir fonksiyonda 
    kullanılmak istendiği zaman başına global yazılmalıdır. Yazılmazsa o alan içinde
    aynı isimde yeni bir local değişken üretir ve global değişkenimiz üzerinde
    hiç bir erişim sağlayamayız. Fonksiyonlarda bu şekilde global değişkenin değerinde
    değişiklik yapmak pek tavsiye edilen bir yöntem değildir. 

    Global bir değişkenin değişken ismi ile local bir değişkenin değişken ismi aynı olabilir. Çünkü
    her değişken, fonksiyon ve class için bir namespace oluşur. Namespace'lerin içerisinde yer alan değişkenler
    o namespace ile ilişkilendirildiği için python yorumlayıcısı hangi değişkenin kullanılmak istendiğini anlayarak
    o namespace'deki o değişkeni çağırarak işlemleri gerçekleştirir. Böylelikle karışıklık yaşanmaz. Ancak
    kod yazarken bu şekilde bir kullanım tavsiye edilmez.

    İç içe oluşturulan fonksiyonlarda fonksiyon tanımı arttıkça local'lik seviyesi artar. En dıştaki 
    fonksiyonun içteki fonksiyonların global değişkenlerine erişimi olurken. İç fonksiyonlara ilerledikçe
    bir üstteki fonksiyonun global değişkenlerine erişim sağlayamaz.

    
    Not: Örnekler fonksiyonlar üzerinden verilecek fonksiyon bilginiz yok ise bu partı
    5.0.fonksiyonlar alanına geldikten sonra inceleyin.
    Not: Değişkene ulaşamayınca NameError hatası alırız. try-except hata yakalama bloğudur.
    İlk şunları dene hata verirse dediğimi yazdır anlamına gelir.
    Not: Fonksiyonlara gönderilen parametreler de local değişken olarak kabul edilir.
    Not: Global değişkenler main içinden tanımlanır. 
"""

c = 30 #global değişken
def function():
    a = 10 # function local değişkeni
    print("fuction içerisinden erişilen c : ",c)
    def insidefunc():
        print("insidefunc içerisinden erişilen c : ",c)
        b = 25 #insidefunc local değişkeni
        print("insidefunc içerisinden erişilen b : ",b)
        print("insidefunc içerisinden erişilen a : ",a)
    insidefunc()
    try:        
        print("fuction içerisinden erişilen a : ",a)
        print("fuction içerisinden erişilen b : ",b)
    except NameError:
        print("b değişkeni insidefunc'nın local değişkeni olduğunu için function'dan erişilemedi.")

function()

print("c global odluğu için her yerden ulaşabiliriz c : ",c)
try:
    print("a local odluğu için her yerden ulaşamayız a : ",a)
    print("b local odluğu için her yerden ulaşamayız b : ",b)
except NameError:
    print("a ve b local değişken olduğu için buradan erişilemez.")

#local alanlardan global değişkenlere erişim
#yanlış kullanım
value = 45 #global değişken
def func():
    value = 20#local değişken
    print("func içinden value : ",value)
func()
print("main içinden value : ",value)

#doğru kullanım
def func2():
    global value 
    value += 20#global değişken
    print("func içinden value : ",value)
func2()
print("main içinden value : ",value)