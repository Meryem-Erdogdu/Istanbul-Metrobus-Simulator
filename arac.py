from log import LogManager

class MetrobusAraci:
    def __init__(self, arac_id):
        self.arac_id = arac_id
        self.durum = "boşta"
        self.hedef_durak = None
        self.log = LogManager("Araç")

    def goreve_basla(self, durak_adi):
        self.durum = "göreve gidiyor"
        self.hedef_durak = durak_adi
        self.log.info(f"{self.arac_id} - Göreve başlıyor: {self.hedef_durak}")
        self._seyahat_simulasyonu()

    def _seyahat_simulasyonu(self):
        from time import sleep
        self.log.info(f"{self.arac_id} - {self.hedef_durak} yönünde hareket ediyor...")
        sleep(2)
        self.durum = "hizmet veriyor"
        self.log.success(f"{self.arac_id} - {self.hedef_durak} durağına ulaştı.")
        
        self.durum = "boşta"
        self.log.info(f"{self.arac_id} - Görev tamamlandı. Durum: {self.durum}")
