import random

def durak_verisini_yukle():
    """
    Rastgele oluşturulmuş İstanbul metrobüs durak verisi döner.
    """
    sabit_duraklar = [
        "Beylikdüzü Sondurak", "Beykent", "Cumhuriyet Mahallesi", "Beylikdüzü Belediye",
        "Beylikdüzü", "Güzelyurt", "Haramidere", "Haramidere Sanayi", "Saadetdere Mahallesi",
        "Mustafa Kemalpaşa", "Cihangir – Üniversite Mahallesi", "Avcılar Merkez Üniversite Kampüsü",
        "Şükrübey", "Büyükşehir Belediye Sosyal Tesisleri", "Küçükçekmece", "Cennet Mahallesi",
        "Florya", "Beşyol", "Sefaköy", "Yenibosna", "Zincirlikuyu", "Mecidiyeköy"
    ]

    duraklar = []
    for i, ad in enumerate(sabit_duraklar, start=1001):
        enlem = round(random.uniform(40.9000, 41.1000), 4)
        boylam = round(random.uniform(28.5000, 29.1000), 4)
        duraklar.append({
            "DURAK_KODU": i,
            "DURAK_ADI": ad,
            "ENLEM": enlem,
            "BOYLAM": boylam
        })

    return duraklar
