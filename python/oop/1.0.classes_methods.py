#OOP
""" 
    Nesne yönelimli programlama (oop), gündelik hayattaki nesneler mantığı
    düşünülerek geliştirilmiş bir programlama yöntemidir. Bir çok işi bünyesinde
    bulunduran bir kod bloğunu bir nesne olarak düşünüp kod yazmak diye açıklayabiliriz.
    Tabi ki bu yöntemi kullanmak için uymamız gereken kurallar vardır. Kendi içinde
    barındırdığı yapılar da (Abstract,Encapsulation,inheritance,polymorphism) vardır. 
    OOP yöntemi kod tekrarını önlediği için kullanımı oldukça yaygındır.
    Sınıf (Class): Nesneleri oluşturmak için kullandığımız şablonlardır. İçerisinde
    birçok değişken, veri yapısı ve metot bulundurur. Her bir metodu nesnenin 
    özelliği olarak düşünebiliriz.
    Nesne (Object): Sınıf şablonları sayesinde oluşturduğumuz ve kullanabildiğimiz
    yapılardır. Özelliklerini sınıfta metot olarak oluştururuz. Bellekte yer kaplarlar.
"""

#Sınıflar (Class)
""" 
    Nesneleri oluşturmak için kullandığımız şablonlardır. İçerisinde
    birçok değişken, veri yapısı ve metot bulundurur. Her bir metodu nesnenin 
    özelliği olarak düşünebiliriz.
    Sınıflar neleri barındırır?
    Sınıf adı,
    Sınıfın nitelikleri,
    Sınıfın metotları,
    __init__ fonksiyonu (constructer),
    Nesnenin nitelikleri,
    Nesnenin metotları,
    Static metotlar bulunur.
"""

#Sınıf Örneği
class Kopek():#sınıf adı
    kopekSayisi = 0 #sınıf niteliği

    def __init__(self, isim, yas):
        self.isim = isim #nesne niteliği
        self.yas = yas #nesne niteliği
        self.km = 0 #nesne niteliği  
        Kopek.kopekSayisiniArttır() 

    def yazdir(self): #nesne metodu
        print("Köpeğimizin ismi : {}, yaşı : {}, yürüdüğü km : {}".format(self.isim,self.yas,self.km))
    
    def yuruyuseCıkar(self,km): #nesne metodu
        self.km +=km

    @classmethod
    def kopekSayisiniArttır(cls): #sınıf metodu "cls" sınıf metodlarında sınıfın elemanlarına ulaşmak için kullanılır.
        cls.kopekSayisi += 1

    @staticmethod
    def bilgi(): #static method
        print("Ben statik methodum.")

kopek = Kopek("pati",2)
kopek.yazdir()
kopek.yas = 3
kopek.yazdir()
kopek.yuruyuseCıkar(4)
kopek.yazdir()
print(Kopek.kopekSayisi)

#__init__ Fonksiyonu (Constructer)
""" 
    init yapıcı fonksiyondur. main alanında obje oluşturduğumuz an çalışacak ilk
    fonksiyondur. Bir sınıfın olmazsa olmazıdır. Nesnenin niteliklerini istersek bu 
    fonksiyon sayesinde obje oluştururken girebiliriz. Yani bu fonksiyon içerisinde
    obje ilk oluşturulduğunda yapılmasını istediğimiz işlevlerin kodunu buraya yazarız.
""" 

#Nesnenin nitelikleri (özellikleri)
""" 
    Nesnenin özellikleri vardır. Mesela bir insanın yaşı vardır, ismi vardır,
    mesleği vardır bunları biz sınıfın içinde değişken olarak tutarız bu değikenlere
    nesnenin nitelikleri deriz. Bu nesnenin niteliklerini main içerisinden 
    değiştirebiliriz. 
"""

#Nesnenin metotları
""" 
    Nesnenin nitelikleri olduğu gibi yaptığı işlerde vardır. Biz normalde işleri
    fonksiyonlarda tanımlayıp kullanırdık. OOP yapısında ise bu fonkisyon dediğimiz
    yapılara metot diyoruz. İş olarak belirttiğimiz şeylerde nesnelerin gerçekleştirmesi
    gereken olaylar olarak düşünebiliriz. Örneğin insanların araba kullanması, uyuması
    gibi gündelik hayattan örnek verebiliriz.
""" 

#Sınıfın nitelikleri
""" 
    Burada da nitelik olarak bahsettiğimiz şey değişkendir. Sınıfın niteliğinden kastımız
    mesela insanların birçok özelliğini saydık ama bunlar nesnin niteliği diye
    sınıflandırıldı ancak insan nüfusu ise insanlık adına bir niteliktir. İşte oop
    mimarisinde de bu tip değişkenlere sınıfın niteliği diyoruz.
    Not: Bu tür değişkenlere sınıfın içinde sınıfın ismi ile ulaşırız.
    Not: Python da sınıf ve nesne niteliği olarak ikiye ayrım mantığı vardır.
    Ancak diğer programlama dillerinde bunu görmek biraz zordur. Pythonda da
    isterseniz sadece nesne niteliği kullanarak yolunuza devam edebilirsiniz.
"""

#Sınıfın Metodu
""" 
    Genelde sınıf niteliği adına oluşturulan metotlardır. @classmethod olarak
    metodun başına yazmamız gerekiyor.
    Not: Bu metodu çağırırken sınıfın ismini kullanarak çağırırız. 
"""

#Statik metot
""" 
    self ya da cls ye gerek duymaz yani sınıf ya da nesne nitelikleri ile işlem
    yapmaz. Kullanımı kısıtlıdır.
"""

