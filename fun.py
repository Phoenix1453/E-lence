import time as t
print("Sistem başlatılıyor...")
t.sleep(2)
print("Hoşgeldin")
karar = str(input("VKİ hesaplayabilir ya da hesap makinesine giriş yapabilirsin \n Hesap Makinesi için hm VKİ için vki yazar mısın : "))

if karar == "hm":
    print("Hesap makinesi başlatılıyor")
    t.sleep(2)
    s = int(input("İlk sayınızı giriniz : "))
    t = int(input("İkinci sayınızı giriniz : "))

    islem = str(input("Yapacağınız işlemi yazınız : "))

    if islem == "*":
        print(s*t)
    elif islem == "-":
        print(s-t)
    elif islem == "+":
        print(s+t)
    elif islem == "/":
        print(s/t)
    else:
        print("Geçersiz İşlem...")

elif karar == "vki":
    print("VKİ Hesaplama başlatılıyor...")
    t.sleep(2)
    b = float(input("Boyunuzu giriniz (180 ise 1.8 olarak vs.) : "))
    k = int(input("Kilonuzu giriniz : "))

    print("Vücut Kitle İndeksiniz Hazırlanıyor...")
    t.sleep(2)
    VKİ = k/(b**2)

    print(VKİ)

    if VKİ < 18.49:
        print("Kilo al kilo")
    elif VKİ < 25:
        print("Kal böyle")
    elif VKİ < 30:
        print("Birazcık kilo versen yeter")
    elif VKİ > 30:
        print("Doktora görün...")
        
else:
    print("Geçersiz Karar...")
