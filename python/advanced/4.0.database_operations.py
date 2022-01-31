""" 
    Veritabanı Nedir?
    Veri setlerinin saklanıp tutulduğu ve ihtiyaç duyulduğunda veriye ulaşılıp
    kullanılan yapılardır.
    Piyasada çoğunlukla ilişkisel veritabanları kullanılır. Bu sayede
    id'lerle birçok tabloyu ilşkilendirebiliyoruz.
    Birçok veritabanı sistemi vardır. Bunlardan birkaç tanesi:
    >SQL Server(Microsoft şirketinin veritabanı)
    >Oracle(Güçlü bir veritabanı)
    >MySQL(PhP geliştiricilerinin sıklıkla kullandığı veritabanı)
    >SQLite(Kurulumu kolay,güçlü ve yaygın veritabanı)
    >MongoDB(No sql veritabanı)
    >POSTGRESQL
"""


import sqlite3


#Veritabanı ile Bağlantı Yapma
connection = sqlite3.connect("files/chinook.db")


#Select Yapısı ile Çalışma
def select():
    """ Verileri getirmemizi sağlayan sql yapısıdır."""
    cursor = connection.execute("""select FirstName,LastName,City from customers 
                                    where City='Prague' or City='Berlin'""")
    print("###Select Yapısı ile Çalışma###")
    for row in cursor:
        print("First Name : ",row[0])
        print("Last Name : ",row[1])
        print("City : ",row[2])
        print("************************")
    connection.close()


#Alfabetik Sıralama Yapma(order by)
def orderby():
    cursor = connection.execute("""select FirstName from employees 
                                    order by FirstName""")
    print("###Alfabetik Sıralama Yapma###")
    for row in cursor:
        print(row[0])

    cursor = connection.execute("""select FirstName from employees 
                                    order by FirstName desc""")
    print("###Ters Alfabetik Sıralama Yapma###")
    for row in cursor:
        print(row[0])
    connection.close()


#Group By Yapısı ile Çalışma
def groupby():
    """ Tabloda veriler arasında gruplama yapan bir komuttur. Bu verilerden 
        kaç tane var gibi. Having ise gruplama sonucu bir koşul koşmak için
        kullanılır."""
    print("###Group By Yapısı ile Çalışma###")
    cursor = connection.execute("""select city,count(*) from customers
                                    group by city having count(*)>1
                                    order by count(*) desc""")
    for row in cursor:
        print(row[0] + "\t" + str(row[1]))
    connection.close()


#Like Komutu ile Çalışma
def like():
    """ Verinin içinde mesela 'b' olanları getir ya da 'c' ile bitenleri getir
        gibi koşulları koymamızı sağlayan komuttur.
        %a% : içinde a olanlar.
        %a  : a ile biten
        a%  : a ile başlayan"""
    print("###Like Komutu ile Çalışma###")
    cursor = connection.execute("""select FirstName,LastName,city from customers
                                    where city like '%w%'""")
    for row in cursor:
        print("First Name : ",row[0])
        print("Last Name : ",row[1])
        print("City : ",row[2])
        print("************************")
    connection.close()


#Insert Yapısı ile Veri Kaydı
def insert():
    """ Var olan veriyi çekmeyi gördük. Şimdi veritabanımıza yeni veriler
        ekleme vaktinin geldiğini düşünüyorum. Gelin beraber bakalım."""
    
    connection.execute("""insert into customers (firstname,lastname,city,email)
                        values('Enes','Sönmez','Istanbul','enesonmezx@gmail.com')""")
    connection.commit()#veritabanına işlenmesi için commit(işlemek) ediyoruz
    connection.close()


#Update Yapısı ile Veri Güncellemsi
def update():
    """ Veritabanına veri kaydettik ama belkide yanlış bir karakter kullandık
        ve bunu düzeltmek istiyoruz ya da veri eklemediğimiz sütuna veri eklemek
        istiyoruz işte bu durumlarda update yapısını kullanacağız.
    """
    connection.execute("""update customers set country = 'Turkey'
                        where firstname='Enes' and lastname='Sönmez' """)
    connection.commit()
    connection.close()


#Del Yapısı ile Veri Silme
def Del():
    """Veritabanına veri ekledik, veri güncelledik şimdi de silme vakti."""
    connection.execute("""delete from customers 
                        where customerid=61""")
    connection.commit()
    connection.close()


#İlişkili Tablolar Arası Veri Çekme
def join():
    """ Sqlite ilişkisel bir veritabanıdır. Tablolar arası id'ler ile ilişki
        kurulur. İlişkiye bağlı olarak verilerin çekilmesi istendiğinde 'join'
        yapısını kullanıyoruz.
        Bu örneğimizde 'albums' tablosu ile 'artist' tablosu arasında bir ilşki var
        bu ilişkiyi kullanarak örneğimizi yapacağız.
    """
    cursor = connection.execute("""select artists.name, albums.title 
                                from artists inner join albums
                                on artists.ArtistId=albums.ArtistId""")
    
    """ from artists inner join albums ile tabloları ilişkilendiriyoruz.
        on ile de tabloların hangi sütunlarının ilişkili olduğunu söylüyoruz."""
    for row in cursor:
        print("Album Name : ",row[0])
        print("Artist Name : ",row[1])
        print("************************")
    connection.close()

connection.close()