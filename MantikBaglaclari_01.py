a = int(input("Birinci sayiyi giriniz: "))
b = int(input("ikinci sayiyi giriniz: "))
c = int(input("ucuncu sayiyi giriniz: "))

if a > b and a < c:
  print("a, b'ye eşit ve aynı zamanda c'den küçüktür")
else:
  print("a, b ile c arasında bir sayı değildir")

if a < b or a < c:
  print("a, b veya c'den daha büyük değildir")
  
if a == b and a < c:
  print("a, b'ye eşit ve aynı zamanda c'den küçüktür")

if a == b and a == c and b==c:
  print("a, b ve ye esittir")
else:
    print("üç sayı birbirine eşit değildir")
    
