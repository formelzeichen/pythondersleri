istenenkredi=100000
hesap=9502
minhes=10000


if hesap>=minhes:
    print("kredi verilebilir.")
    print("ödemeler hesaplandı.")
elif hesap>=9000 and hesap<=9500:
    print("Müdüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("Genel Müdüre sorulacak")
else:
    print("kredi almak için bakiyeniz yetersiz.")



print("işlem sonu")