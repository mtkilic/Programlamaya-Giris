birinci_sayi = int(input("Birinci sayiyi giriniz: "))
ikinci_sayi = int(input("ikinci sayiyi giriniz: "))

if birinci_sayi == ikinci_sayi:
  print("sayilar esittir\nsayilar farkli degildir\nilk sayi kucuk degildir\nikinci sayi kucuk degildir\nilk sayi kucuk esittir\nikinci sayi kucuk esittir")

elif birinci_sayi != ikinci_sayi:
  print("sayilar esit degildir\nsayilar farklidir")
  if birinci_sayi < ikinci_sayi:
    print("ilk sayi kucuktur")
  if ikinci_sayi > birinci_sayi:
    print("ikinci sayi kucuktur degildir")
  if birinci_sayi <= ikinci_sayi:
    print("ilk sayi kucuk esittir")
  if ikinci_sayi <= birinci_sayi:
    print("ikinci sayi kucuk esittir")
