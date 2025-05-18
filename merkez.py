from arac import MetrobusAraci
from log import LogManager

class Merkez:
    def __init__(self):
        self.arac_listesi = []
        self.atanan_arac = {}
        self.log = LogManager("Merkez")

    def arac_ekle(self, arac_id):
        yeni_arac = MetrobusAraci(arac_id)
        self.arac_listesi.append(yeni_arac)

    def durak_raporla(self, rapor):
        durak = rapor["durak"]
        seviye = rapor["kalabalik_seviyesi"]

        if seviye > 25:
            self.log.alert(f"🚨 Yüksek kalabalık tespit edildi: {durak} - Araç yönlendiriliyor...")
            self.arac_gonder(durak)
        elif 15 <= seviye <= 25:
            self.log.warning(f"⚠️ Orta kalabalık: {durak} - Bekleniyor...")
        else:
            self.log.info(f"🟢 Normal kalabalık: {durak}")

    def arac_gonder(self, durak_adi):
        for arac in self.arac_listesi:
            if arac.durum == "boşta":
                arac.goreve_basla(durak_adi)
                self.atanan_arac[durak_adi] = arac.arac_id
                self.log.success(f"✅ {arac.arac_id}, {durak_adi} durağına yönlendirildi.")
                return
        
        # Eğer hiç bir araç boşta değilse, bir uyarı ver
        self.log.error("❌ Uygun araç bulunamadı!")
