""" Listeler verilerimizi bir arada tutmamızı sağlayan bir veri tipidir. Genel programlama
    jargonunda Array olarakta bilinir. 
    Listede eleman değişikliği yapabiliriz.
    Birden fazla ilkel veri tipini aynı listeye ekleyebiliriz.
    İç içe listeler oluşturabiliriz."""

liste = ["Samsun",55,12.5,True]
iciceliste = ["Trabzon",61,["Aydın",9]]

#Listedeki Elemanlara Ulaşma (İndisleme)
print(iciceliste[0]) # [-1] veya [len(list_name) - 1] ile son liste elemanına ulaşabiliyoruz.
print(iciceliste[2][0])

#Lİste Slice (Dilimlemek)
""" Belli liste eleman aralığını almamızı sağlar."""
liste2 = liste[:2] #Başlangı. indisinden 2. indise kadar değerleri alıp liste2'ye atar.

#Concatenation (Birleştirme) and Repetition (Tekrarlama)
mergelist = liste + [1,2,3,4] #["Samsun",55,12.5,True,1,2,3,4]
repeatlist = [1,2,3,4] * 2  #[1,2,3,4,1,2,3,4] 

#Liste Değişebilirlik (Mutability)
""" Liste elemanlarını yeni veriler ile değiştirebiliyoruz. Aynı zamanda liste veri tipi hem birleştirilebilme hem de
    ekleme özelliğini barındırır."""

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)


#Listeye Eleman Ekleme
""" Dinamik listeler oluşturmak için ekleme özelliği çok önemlidir. Gelin birkaç ekleme biçimine bakalım:"""
list_one = ["first element"]
#1. Yol
list_one +=["second element"]
list_one = list_one + ["third element"]
#2. Yol
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
#3. Yol
""" append(): Bu metod listeye eleman eklememizi sağlar."""
list_one.append("forth element")
#4. Yol
""" insert(): Eklenecek elemanı istenilen indise eklemeye yarar. """
list_one.insert(1,"more element")
print(list_one)

#Listeden Eleman Silme
""" Dinamik bir liste oluşturmak istiyorsanız ekleme işlemi kadar silme işlemide önem arz etmektedir.
    Birkaç tane liste elemanı silme tarzı vardır: 
    pop(): Listedeki son elemanı siler. Ancak verilen indiside siler.
    clear(): Listenin içeriğini tamamen siler.
    del: Belli bir indis aralığını veya belli bir indisi siler.
    remove(): İstenilen elemanı yazarak silinmesini sağlarız."""
list_two = list_one
list_two.pop()
list_two.pop(1)
print(list_two)
list_two.clear()
print(list_two)
list_two = [1,2,3,4,5,6]
del list_two[0:2]
print(list_two)
list_two.remove(3)
print(list_two)

alist = ['a', 'b', 'c', 'd', 'e', 'f'] #Kullanılması önerilmez
alist[1:3] = []
print(alist)

""" Listenizin bir klonunu oluşturmak isterseniz atama işleminden kaçınmanızı öneririm. Çünkü klon listenizdeki
    her değiişklik orjinal listenizde de değişikliğe sebebiyet verir. Bunu engellemek için copy() metodunu veya 
    slice yöntemini kullanabilirsiniz."""
#Slice Yöntemi
a = [81,82,83]
b = a[:]       
print(a == b) #True (değerlere bakılır)
print(a is b) #False (referans bellek bölgesine bakılır)
#Copy Metodu Yöntemi
a = [81,82,83]
b = a.copy()
print(a == b) #True (değerlere bakılır)
print(a is b) #False (referans bellek bölgesine bakılır)


#Liste Metotları
""" Listenin içinde bulunan bir string değere ulaşarak string metotlarını kullanabilirsiniz.
    Ancak 'len' metodunda küçük bir fark vardır.
    len(): listede kaç eleman olduğunu gösterir.
    index(): Listedeki istenilen elemanın indisini döndürür. Listede olmayan bir veri aratırsanız hata alırsınız.
    count(): Listede, count fonksiyonunun içine yazılan veriden kaç tane var sorusuna cevap döndürür.
    copy(): Listeyi kopyalar. Ancak diğer listedeki değişiklik kopyalanan listeyi etkilemez.
    reverse(): Listeyi tersine çevrir.
    sort(): Listeyi küçükten büyüğe ya da büyükten küçüğe sıralamaya yarar.
    extend(): Listeleri birleştirir.
    list(): Boş liste oluşturur veya string bir değeri karakter karakter listeye çevirir.
    Aynı zamanda diğer koleksiyon tiplerini listeye çeviriyor.
    """
print(liste[0].count("s"))
print(len(liste))

sayilar = [54,122,12,2,85,12,32]

print(sayilar.index(85))
copy_list = sayilar.copy()
print(copy_list)
sayilar.reverse()
print(sayilar)
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)

copy_list.extend(sayilar)
print(copy_list)

b = list()
print(b)
name = "john"
b = list(name)
print(b)

#Tuple - list dönüşümü
demet = (12,25,32)
print(type(demet))
donusum = list(demet)
print(type(donusum))