while True:
    #Python'da input kismi her zaman string olarak output verir. O yuzden int() fonksiyonu ile girelen degeri tam sayiya geviriyoruz
    #try ve except ile hatayi buluyoruz. 
    try:
        sayi = int(input("Bir sayi giriniz:  "))
        break
    #Eger tam sayi haricinde bir deger girilirse, ValueError verir
    except ValueError:
    #ValueError hatasi alintigidinda altdaki print fonksoyunu devreye girer
        print("Lutfen sadece tam sayi giriniz.")


print("Girdiginiz sayi: {}".format(sayi))
