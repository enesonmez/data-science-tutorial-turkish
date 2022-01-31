""" 
    Bu konu çok biçimliliğe benzer. Ancak farkları vardır. Bu konuda da bir sınıf
    bir veya  daha fazla sınıf ile kalıtılmalıdır. Bunun yanı sıra polymorphism de
    olduğu gibi aynı isimden her sınıfta method oluşturulmalıdır. Ancak base class
    taki sınıfın içi boş bırakılmalıdır. İşte polymorphism'den ayıran nokta burasıdır.
    Biz burada şunu söylüyoruz. Bu sınıfın şu işlevi vardır ancak bu işlev her child class
    için farklı olduğu için genel bir işlev tanımlıyamıyorum. Ben bunları child class'larda
    tanımlayacağım anlamına gelir. Biz oluşturduğumuz base class'a nesne oluşturup çağırırsak
    hata alırız.
    Not: abstract yapısı python'da varsayılan olarak yoktur. Biz bu yapıyı
    kütüphane ile import ederiz.
"""

from abc import ABC,abstractmethod

class Animal(ABC):
    def live(self):
        print("living")
    
    @abstractmethod
    def run(self): pass

class Wolf(Animal):
    def __init__(self):
        self.live()
    
    def run(self):
        print("running")

a1 = Wolf()
a1.run()