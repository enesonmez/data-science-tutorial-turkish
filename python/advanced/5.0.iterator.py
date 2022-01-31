""" 
    iterasyon : bir listenin (koleksiyonların tümü) tüm verilerini tek tek dolaşma mantığıdır.
    Mesela bir for döngüsü arkada bir iterator çalıştırır.
    Not: listenin adedinden fazla çağırım yapılırsa hata verir.
"""

city = ["Istanbul","Ankara","Samsun"]

iterator = iter(city)

print(next(iterator))
print(next(iterator))
print(next(iterator))


""" 
    Sınıf içerisinde kendi iterator'larımızı oluşturabiliriz. Gelin birlikte 
    bakalım.
"""


class MyNumbers:
    def __init__(self,maxi):
        self.maxi = maxi

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.maxi:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration


myclass = MyNumbers(5)
myiter = iter(myclass)

for x in myiter:
  print(x)

""" 
    Iterator bir olarak bir nesne / sınıf oluşturmak için, nesnenize 
    __iter __ () ve __next __ () yöntemlerini uygulamanız gerekir.
    __iter__() her zaman iterator nesnesinin kendisini döndürmelidir.
    __next__() bir sonraki öğeyi döndürmelidir.
    StopIteration : iterasyonun sozsuza dek gitmemesi için kullanılır.
"""