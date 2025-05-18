# Istanbul-Metrobus-Simulator
Bu proje, Bilgisayar Ağ Sistemleri dersi kapsamında geliştirilmiştir. İstanbul'daki metrobüs sistemini simüle eden, her duraktaki rastgele kalabalık tespiti yapan ve buna göre metrobüs araçlarını yönlendiren bir sistemdir. Tamamen Nesne Tabanlı Programlama (OOP) ile yazılmıştır ve CSV dosyasına bağımlılık olmadan çalışır. Tüm veriler rastgele üretilir ve gerçek zamanlı olarak loglanır.

Özellikler
- Kalabalık Tespiti : Her durakta bir kamera nesnesi vardır. Bu kamera, rastgele sayılarla kalabalığı simüle eder.
- NVR Cihazı : Kamera verisini alır ve Merkez'e iletir.
- Merkez Kontrol Sistemi : Gelen raporlara göre yüksek kalabalık tespit edilen duraklara boşta olan metrobüsleri yönlendirir.
- Loglama Sistemi : Tüm işlemler INFO, WARNING, ERROR, SUCCESS gibi seviyelerde loglanır.
- Random Veri Üretimi : Gerçek bir CSV dosyasına gerek yoktur. Rastgele oluşturulan durak verisi ile çalışır.
- Modüler Yapı : Her sınıf ayrı bir dosyada olup, sistemin farklı bileşenleri arasında haberleşme sağlanır.

 
![Ekran görüntüsü 2025-05-19 003456](https://github.com/user-attachments/assets/0a4d43e9-aaac-4377-af22-d3a7bd4b3cd5)
