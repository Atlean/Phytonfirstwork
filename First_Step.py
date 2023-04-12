x=float(input("Lütfen ilk sayıyı verin: "))
y=float(input("Lütfen ikinci sayıyı verin: "))
z=float(input("Lütfen üçüncü sayıyı verin: "))
print("Sayıların çarpımları {}".format(x*y*z))


kilo =int(input("Lütfen kilonuzu giriniz : "))
boy = float(input("Lütfen boyunuzu noktalı giriniz (örnek 1.76): "))

Vki = kilo/(boy * boy)
print(Vki)



tüketim = float(input("Aracınız km'de kaç litre benzin yakıyor?(noktalı giriniz.)"))
yol = float(input("Aracınız ile kaç km yol yaptınız ?(noktalı giriniz)"))
Para = yol*tüketim*22.41
print("yaktığınız tutar tam olarak:{}".format(Para))


ad = input("Lütfen adınızı giriniz: ")
soyad = input("Lütfen soy isminizi giriniz: ")
numara = input("Lütfen numaranızı giriniz: ")
print("adınız {} \nsoyadınız {} \nnumaranız {}".format(ad,soyad,numara))

dik=float(input("Dik kenarın uzunluğu: "))
taban=float(input("tabanın uzunluğu: "))
c = (dik**2+taban**2)**0.5
print("Hipotenüs:",c)

k=int(input("a:"))
l=int(input("b:"))
m=int(input("c:"))

delta = l**2 - 4 * k * m

x1 = (-l-delta**0.5)/(2*k)
x2 = (l-delta**0.5)/(2*k)

print("birinci kök: {}\n ikinci kök: {}".format(x1,x2))

a = int(input("Lütfen ilk sayıyı girin: "))
b = int(input("Lütfen ikinci sayıyı girin: "))
a,b = b,a              "burası sayıları değiştirme yeri"
print("{} {}".format(a,b))

