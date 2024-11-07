# eticaretmerkezim_AI_V1.0
 E- Ticaret Merkezim şirketi, Trendyol, Hepsiburada, Pazarama gibi e-ticaret üzerine çalışan firmalara Google SEO çalışmaları üzerine veri bilimi alanında danışmanlık hizmeti vermektedir. Gönüllü stajyerliğim süresince, şirket çalışanları tarafından manuel olarak gerçekleştirilen ve veri bilimi üzerine olan çalışmaların, yapay zeka kullanılarak otonomlaştırılmasını sağlayarak insan hatasından kaynaklı gecikmeleri minimize etmeye çalışmak oldu.
## eticaretmerkezim AI V1.0 neler yapıyor?

GÖRSEL

- Bir excelde linkler halinde gelen ürün verilerinin görsellerini indirebiliyor.
- İndirilen görselleri tanıyabiliyor ve özellik çıkarımı gerçekleştiriyor. (İlk versiyonunda sadece renk özellikleri için)
- Tahmin ettiği ürün renklerini veriyi çektiği excelde yeni bir sütun açarak yazıyor.
- Güncellenmiş excel dosyasını kaydediyor.
- Kullanımı kolay arayüzü sayesinde teknik bilgisi olmayan ofis çalışanları rahatça kullanabiliyor.

## Veri Seti
Modelin eğitimi için 1521 adet görsel içeren bir veri seti hazırlanmıştır, etiketleme ve düzenleme gibi işlemler Roboflow sitesinde gerçekleştirilmiştir. Veri setinde sınıfların dağılım oranı olabildiğince birbirine yakın sayılırda olmaya gayret edilmiştir. Veri setinin %70'i train, %15'i validasyon ve %15'i test edilmek üzere ayrıştırılmıştır. Model eğitiminde kullanılan hazır veri setine ulaşmak için: https://www.kaggle.com/datasets/emircanakyuz/womens-clothing-dataset

## Kullanılan Yapay Zeka Modeli
eticaretmerkezim-AI V1.0 bir MVP ürünüdür de diyebiliriz, yani geliştirilebilecek bir yazılım ürününün ilk versiyonu. Yazılımın merkezinde "Kadın Elbise" kategorisinde çeşitli görseller ile eğitilmiş bir yapay zeka modeli yer almaktadır. Yapay zeka modelinde mimari olarak Konvolüsyonel Sinir Ağları (Convolutional Neural Networks, CNN) kullanılmıştır. Mimaride 3 konvulasyon katmanı bulunmakta ve her konvulasyon katmanından sonra max pooling katmanı gelmektedir. Ayırca her katmanda belirli oranda nöronların devre dışı kaldığı dropout yöntemi kullanılmıştır. Sınıflandırma katmanında ise 9 ayrı sınıfımız olduğu için 9 nöron bulunmaktadır, bu sınıflar:
- 0: Renkler,
- 1: Bej,
- 2: Beyaz,
- 3: Çok Renkli,
- 4: Gri,
- 5: Lacivert,
- 6: Mavi,
- 7: Pembe,
- 8: Siyah
Model mimarisi hakkında daha detaylı bilgiye "create_model" klasöründeki "model.py" ve "model_mimarisi.jpg" isimli dosyalardan ulaşabilirsiniz.

## Performans
Model eğitiminde doğruluk ve hata (loss) grafikleri aşağıdaki gibidir.

GÖRSEL

Eğitim sonucunda modelin genel ve sınıf bazlı performansı analiz edilmiştir, sonuçlar aşağıda paylaşılmıştır.

GÖRSEL

Modelin renkleri tahmin etme performansı %91' dir. Bazı renklerde bu oran %98' lere kadar çıkabiliyorken bazılarında ise %79' a kadar gerilemektedir.
