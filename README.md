# 📱 QR Kod Oluşturucu

Metin ve URL'leri kolayca QR koduna dönüştüren, modern ve kullanıcı dostu bir web uygulaması.

## ✨ Özellikler

- 🎨 **Modern UI** - Tailwind CSS ile güzel tasarım
- 📱 **Responsive** - Tüm cihazlarda uyumlu
- ⬇️ **İndir** - QR kodları PNG olarak indir
- 📤 **Paylaş** - Web Share API ile paylaş
- 📋 **Kopyala** - Panoya kopyalama desteği
- 🔒 **Güvenli** - Input validasyonu ve XSS koruması
- ⚡ **Hızlı** - Optimize edilmiş performans
- 🛡️ **Hata Yönetimi** - Kapsamlı error handling

## 🚀 Kurulum

### Ön Gereksinimler
- Python 3.8+
- pip

### Adımlar

1. **Repository'yi klonla**
```bash
git clone https://github.com/hilmiturksoy/qr-app.git
cd qr-app
```

2. **Sanal ortam oluştur**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Gerekli paketleri yükle**
```bash
pip install -r requirements.txt
```

4. **.env dosyasını oluştur** (isteğe bağlı)
```bash
cp .env.example .env
```

5. **Uygulamayı çalıştır**
```bash
python app.py
```

6. **Tarayıcıda aç**
```
http://localhost:5000
```

## 📖 Kullanım

1. Ana sayfada metin veya URL gir
2. "QR Kod Oluştur" butonuna tıkla
3. QR kodu görüntüle ve:
   - İndir (PNG dosyası olarak)
   - Paylaş (destekleyen cihazlarda)
   - Panoya Kopyala
   - Yeni QR Oluştur

## 🔌 API Endpoints

### POST /api/qr
QR kod oluşturma API'si

**İstek:**
```json
{
  "text": "https://github.com",
  "size": 10,
  "border": 2
}
```

**Yanıt:**
```json
{
  "success": true,
  "qr_code": "data:image/png;base64,..."
}
```

## 📁 Proje Yapısı

```
qr-app/
├── app.py                 # Flask uygulaması
├── qr_creator.py         # CLI QR kod oluşturucu
├── requirements.txt       # Proje bağımlılıkları
├── .env.example          # Ortam değişkenleri örneği
├── .gitignore            # Git ignore kuralları
├── README.md             # Bu dosya
└── templates/
    ├── index.html        # Ana sayfa
    ├── 404.html          # 404 hata sayfası
    └── 500.html          # 500 hata sayfası
```

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **QR Kodu**: qrcode-python
- **Görsel İşleme**: Pillow

### Yapılan İyileştirmeler

1. **Hata Yönetimi**
   - Input validasyonu
   - Try-catch error handling
   - Kullanıcı dostu hata mesajları
   - Custom error pages

2. **Güvenlik**
   - XSS koruması
   - CSRF koruması (Flask default)
   - Input sanitization
   - Max content length limitesi

3. **Performans**
   - Buffer optimizasyonu
   - Lazy loading desteği
   - Optimized CSS ve JS

4. **UX/UI**
   - Loading gösterimi
   - Animasyonlar
   - Responsive design
   - Modern tasarım

5. **Kod Kalitesi**
   - Docstring'ler
   - Logging
   - Modüler yapı
   - Best practices

## 🖥️ CLI Kullanımı

QR kod komut satırından da oluşturabilirsiniz:

```bash
# Basit kullanım
python qr_creator.py "https://github.com"

# Çıktı dosyasını belirt
python qr_creator.py "Merhaba Dünya" -o output.png

# Yardım
python qr_creator.py --help
```

## 🐛 Hata Raporlama

Bir hata bulduysanız, lütfen [Issues](https://github.com/hilmiturksoy/qr-app/issues) kısmında rapor et.

## 📝 Lisans

Bu proje MIT lisansı altında yayınlanmıştır.

## 👤 Geliştirici

**Hilmi Türkşoy**
- GitHub: [@hilmiturksoy](https://github.com/hilmiturksoy)

## 🤝 Katkıda Bulunma

Pull request'ler açığız! Büyük değişiklikler için lütfen önce bir issue aç.

---

**Son Güncelleme**: 2025-06-13 | **Versiyon**: 2.0
