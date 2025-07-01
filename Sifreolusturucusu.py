import random
import string

def sifre_uret(uzunluk=12, buyuk_harf=True, kucuk_harf=True, rakam=True, ozel_karakter=True):
    karakterler = ""
    if buyuk_harf:
        karakterler += string.ascii_uppercase
    if kucuk_harf:
        karakterler += string.ascii_lowercase
    if rakam:
        karakterler += string.digits
    if ozel_karakter:
        karakterler += string.punctuation

    if not karakterler:
        return None

    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

def guvenlik_degeri(sifre):
    puan = 0

    # Uzunluk
    if len(sifre) >= 8:
        puan += 2
    if len(sifre) >= 12:
        puan += 2

    # Karakter çeşitleri
    if any(c.islower() for c in sifre):
        puan += 2
    if any(c.isupper() for c in sifre):
        puan += 2
    if any(c.isdigit() for c in sifre):
        puan += 2
    if any(c in string.punctuation for c in sifre):
        puan += 2

    # Puan 0-10 arası olur
    if puan >= 8:
        return "Güçlü"
    elif puan >= 5:
        return "Orta"
    else:
        return "Zayıf"

def main():
    print("Şifre Üretici")
    uzunluk = int(input("Şifre uzunluğu (örn. 12): "))
    buyuk = input("Büyük harf kullanılsın mı? (evet/hayır): ").lower() == "evet"
    kucuk = input("Küçük harf kullanılsın mı? (evet/hayır): ").lower() == "evet"
    rakam = input("Rakam kullanılsın mı? (evet/hayır): ").lower() == "evet"
    ozel = input("Özel karakter kullanılsın mı? (evet/hayır): ").lower() == "evet"

    sifre = sifre_uret(uzunluk, buyuk, kucuk, rakam, ozel)
    if sifre is None:
        print("Lütfen en az bir karakter türü seçin.")
        return

    print("\nOluşturulan Şifre:", sifre)
    print("Güvenlik Seviyesi:", guvenlik_degeri(sifre))

if __name__ == "__main__":
    main()
