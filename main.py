from veri import durak_verisini_yukle
from durak import Durak
from kamera import KalabalikKamera
from nvr import NVR
from merkez import Merkez
import time

def simulasyon():
    print("Metrobüs sistemi başlatılıyor...")
    raw_data = durak_verisini_yukle()

    if not raw_data:
        print("Veri yüklenemedi.")
        return

    durak_nesneleri = [
        Durak(item["DURAK_KODU"], item["DURAK_ADI"], item["ENLEM"], item["BOYLAM"])
        for item in raw_data
    ]

    kameralar = [KalabalikKamera(durak.ad) for durak in durak_nesneleri]
    nvrlar = [NVR(kamera) for kamera in kameralar]

    merkez = Merkez()
    for i in range(20):
        merkez.arac_ekle(f"Metrobus_{i+1}")

    print("Simülasyon başladı...\n")
    while True:
        print("\n=== İSTANBUL METROBUS DURAK RAPORLARI ===")
        for nvr in nvrlar:
            rapor = nvr.veri_al_ve_gonder()
            merkez.durak_raporla(rapor)
        time.sleep(3)

if __name__ == "__main__":
    simulasyon()
