""" 
    CSV, Virgülle Ayrılmış Değerler (Comma Split Values) anlamına gelen bir kısaltmadır. 
    CSV biçimindeki bir dosya, yalnızca belirli kuralları izleyen bir metin dosyasıdır.
    Kural olarak bahsettiğimiz bu durum saklamak istediğiniz farklı verileri virgül ile
    ayırıyorsunuz ve bunu benzer veriler ile satır satır çoğaltabiliyorsunuz.

    Buradaki işlem aslında excel programındaki gibi satır sütun işlemleridir. CSV dosyasındaki
    her virgülle ayrılmış veri bir sütunu temsil eder. Her veri satırı ise exceldeki bir satırı temsil eder.
    Böyle bir dosya oluşturup .cvs uzantısı ile kaydederseniz ve excel veya benzer bir programda açarsanız
    dosyanızın satırlara ve sütunlara ayrıldığını göreceksiniz.

    Her bir sütunu isimlendirmek isterseniz dosyaya ilk olarak sütunların ismini yazarak başlamanız daha
    sonrasında verileri girmeniz gerekir.

    CSV dosya formatı ile çoğunlukla veri bilimciler çalışmaktadır. Genelde modeli eğitmek için gerekli verilerin 
    saklanması ve işlnemesi için kullanılan formatlardan biridir.
"""


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]
             

# Dosya yazma işlevi ile csv dosyasına yazma
outfile = open("files/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


#csv modülü ile yazma
import csv

with open('files/reduced_olympics.csv', 'w', newline="") as file:
    writer = csv.writer(file, delimiter=",")
    fnames = ['Name', 'Age', 'Sports']
    writer.writerow(fnames)
    for olympian in olympians:
        row_string =[olympian[0], olympian[1], olympian[2]]
        writer.writerow(row_string)


#csv modülü ve sözlük veri tipi ile yazma
olympians = [{"Name":"John Aalberg", "Age" : 31, "Sports" : "Cross Country Skiing"},
             {"Name":"Minna Maarit Aalto", "Age" : 30, "Sports" : "Sailing"},
             {"Name":"Win Valdemar Aaltonen", "Age" : 54, "Sports" : "Art Competitions"},
             {"Name":"Wakako Abe", "Age" : 18,  "Sports" : "Cycling"}]

with open('files/reduced_olympics.csv', 'w', newline="") as file:
    fnames = ['Name', 'Age', 'Sports']
    writer = csv.DictWriter(file, fieldnames=fnames, delimiter=",")    

    writer.writeheader()
    for olympian in olympians: #olympian sözlük veri tipidir.
        writer.writerow(olympian)


#Dosya okuma işlevi ile csv dosyasını okuma
outfile = open("files/reduced_olympics.csv", "r")
lines = outfile.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    print(row.strip())
outfile.close()


#csv modülü ile okuma
with open('files/reduced_olympics.csv', 'r') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        print(row)


#csv modülü, sütun isimleri verilen csv dosyaları için okuma yöntemi
with open('files/reduced_olympics.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row['Name'], row['Age'], row['Sports'])