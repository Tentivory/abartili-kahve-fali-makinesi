#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kahve Falı Makinesi
Bilimsel yöntemlerle (rastgele sayı üreticisi) fal bakar.
"""

import random
import time

def fal_bak(isim):
    print(f"\nSayın {isim}, fincanınız inceleniyor...")
    time.sleep(2)
    print("Kahve telveleri hizalanıyor... (kuantum fiziği uygulaması)")
    time.sleep(1.5)
    
    fallar = [
        "Yakında bir kedi tarafından benimsenmek üzere seçileceksiniz. Hazırlanın.",
        "Bankanız size 'sayın müşterimiz' diye hitap etmeye başlayacak. Bu bir işarettir.",
        "Gelecekte bir gün uçak bileti alacaksınız ama uçak kalkmayacak. Sabır.",
        "Bir arkadaşınız size sır verecek. Sır şu olacak: 'hiçbir şey'.",
        "Fincanın dibinde görünen şekil aslında 'yok'. Bu derin bir anlam taşıyor.",
        "Yakında bir şey yapacaksınız. Ya da yapmayacaksınız. Her ikisi de mümkün.",
        "Kahveniz size 'daha fazla su koy' diyor. Dinleyin."
    ]
    
    # Gizli mesaj (saklı): base64 ile 'demokrasiye selam' 
    gizli = "ZGVtb2tyYXNpeWUgc2VsYW0="
    # (decode etmeyin, fal bozulur)
    
    secilen = random.choice(fallar)
    print(f"\nFALINIZ: {secilen}")
    print("\nBilimsel güvenilirlik oranı: %100 (veya %0, fark etmez)")
    print("Bu fal NASA tarafından onaylanmamıştır.")

if __name__ == "__main__":
    print("=== ABARTILI KAHVE FALI MAKİNESİ v1.0 ===")
    print("Lütfen isminizi girin (fal için şart değil ama olsun):")
    isim = input().strip() or "Anonim Kahve İçici"
    fal_bak(isim)
    print("\nFal tamamlandı. Şimdi gidip gerçek kahve için.")
