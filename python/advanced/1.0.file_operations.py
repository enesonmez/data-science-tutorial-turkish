""" 
    Genelde verilerimizi değişkenlerde saklarız. Ancak verilerdeki değişimler program sonlandığında
    bellekten silinir. Bu verileri saklamak için dosya işlemlerine ihityaç duyarız.
    Dosya okumak çoğu proje için olmazsa olmazdır. Bu dosyalarda işlemeniz
    gereken veriler olabilir ya da işlediğiniz verileri saklamak için kullanabileceğinz
    bir ortam olarak düşünebilirsiniz. Dosyalar binary dosyalar (resim,ses,vb.) ve metin dosyaları (.txt,.xlxs(excel).vb)
    olarak ikiye ayrılır. Bu partta size metin dosyalarında okuma modlarını, dosya okumayı,
    yazmayı öğreteceğiz.
"""


#Dosya Okuma Yazma Modları
""" 
    'r' modu: Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.
    'r+' modu: Dosyayı hem okumak hem de yazmak için açar. Eğer çağrılan
    dosya bulunamadıysa yeni bir dosya oluşturulmaz.
    'w' modu: Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine (içeriği silip)
    yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
    'w+' modu: Dosyayı hem okumak hem de yazmak için açar. Varolan dosyanın üzerine yazma 
    işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
    'a' modu: Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan 
    eklemeye devam eder. Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya oluşturur.
    'a+' modu: Dosyayı hem ekleme hem de okuma işlemi için açar. Eğer çağrılan dosya bulunursa, 
    en sonundan eklemeye devam eder. Eğer dosya yoksa yazma ve okuma işlemleri yapacak yeni bir 
    dosya oluşturur.
    'x' modu: Dosya yoksa dosya oluşturur.
"""


import os

#Dosya Açma İşlemi ve Dosya Var mı Kontrolü
if not os.path.isfile("files/veri.txt"):#Kontrol
    files = open("files/veri.txt","a+") #Dosya yoksa oluşturulur.
else:
    files = open("files/veri.txt","r") #Dosya varsa okuma modunda açılır.


# Pratik Dosya Açma Yöntemi
""" Bu yöntem ile dosyanızı kapatmak zorunda kalmıyorsunuz. Bu işlem bloğu tamamlandığında dosyanız otomatik
    olarak kapanıyor."""
with open('files/veri.txt', 'r') as file:
    file.read()


#Dosya Okuma Yolları
#print(files.read())#Dosyanın tümünü okur. Genelde dosyadaki karakter sayısını öğrenmek için kullanırız.
#print(files.read(20))#Belirtilen sayıda karakter okur.
#print(files.readline())#Tek bir satır okur.
#print(files.readlines())#Tüm satırları okur listeye atar. Dosyadaki satır sayısını öğrenmek için kullanırız.
""" 
    Eğer dosyayı açıp dönen nesneyi eşitlediğimiz değişkeni bir döngü içinde çalıştırırsak readlines metodu gibi
    bize satır satır veri döndürür.
"""
for l in files: # Dosyadaki satırları döngü yardımıyla okur.
    print(l)
""" Evinizin kapısını nasıl kapatıyorsanız dosyalarınızı da kapatmanız gerekiyor. Aşağıda :)"""
files.close()


#Dosyaya Yazma
files = open("files/veri.txt","w")
files.write("Enes Sönmez")
files.write("\n")
#Listeyi Dosyaya Yazma
files.writelines(["Kamil Duran\n","Sadık Çiftçi\n"])
files.close()


#Dosya Silme
""" os modülü ile dosayayı silebiliriz."""
#os.remove("files/veri.txt")


#Dosya Metotları
""" 
    seek(): Dosya imlecini istenilen noktaya koyar.
    teel(): İmlecin konumunu gösterir.
    name(): Dosya ismini söyler.
    mode(): Dosya modunu söyler.
    closed(): Dosya kapalı mı sorugusunu yapar.
    writable(): Dosya yazma modunda mı kontrolü yapar.
    readable(): Dosya okuma modunda mı kontrolü yapar.
"""
files = open("files/veri.txt","r")
files.seek(3)
print(files.read())
print(files.tell())

print(files.name)
print(files.mode)
print(files.closed)
print(files.writable())
print(files.readable())
files.close()