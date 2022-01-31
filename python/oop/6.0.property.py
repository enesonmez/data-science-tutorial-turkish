""" 
    Property, classların içindeki metodları nitelik (değişken) haline getirmeye
    yarayan bir yapıdır. 
"""

class Kitap():
    def __init__(self,baslik):
        self.__baslik = baslik

    @property
    def baslik(self):
        return self.__baslik
    
    @baslik.setter
    def baslik(self,baslik):#property ile oluşturulmuş niteliğin değerini değiştirme
        self.__baslik = baslik
    
    @baslik.deleter
    def baslik(self):#property ile oluşturulmuş niteliği siler.
        del self.__baslik

    

k1 = Kitap("Otostopçunun Galaksi Rehberi")
print(k1.baslik)

""" 
    Şuan property ile oluşturulmuş baslik metodu sadece okunabilir durumda
    içerik değiştirmeye imkan vermiyor. Ancak bunu çözecek imkanımız bulunuyor.
    Aynı isimde bir method daha oluşturuyoruz ve metodun başına @metod adı.setter
    yazıyoruz. Metodun içinede atama işlemlerini yazıyoruz.
"""

k1.baslik = "Sefiller"
print(k1.baslik)

del k1.baslik

""" 
    Özetle property decoreter'ı kendine ek olarak setter ver deleter decoreter'larını da
    barındırarak metodları nitelik yani değişken haline dönüştürmeye yarar.
"""