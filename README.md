# Sabah Botu ☀️

Her sabah Türkiye saatiyle 09:00'da Telegram'a güncel hava durumunu, dolar ve euro kurunu ve gram altın fiyatını gönderen bir Python botu. GitHub Actions sayesinde bilgisayar kapalıyken bile kendi kendine çalışır.

## Örnek Mesaj

```
Günaydın :)

Sıcaklık: 14.2 °C
Dolar: 50.57 TL
Euro: 55.58 TL
Altın: 5959.75 TL
```

## Nasıl Çalışır?

1. **Open-Meteo API**'den anlık sıcaklık çekilir.
2. **Frankfurter API**'den dolar ve euro kurları ile altının ons fiyatı çekilir; ons fiyatı grama çevrilir.
3. Tüm bilgiler tek bir mesajda birleştirilir.
4. Mesaj **Telegram Bot API** ile gönderilir.
5. **GitHub Actions**, bu işlemi her gün belirlenen saatte otomatik olarak başlatır.

## Kullanılan Teknolojiler

- **Python**: requests, python-dotenv
- **Open-Meteo API**: hava durumu
- **Frankfurter API**: döviz kurları ve altın fiyatı
- **Telegram Bot API**: mesaj gönderme
- **GitHub Actions**: zamanlanmış otomatik çalıştırma

## Kurulum

1. Repoyu bilgisayarına indir:
   ```bash
   git clone https://github.com/arzubingul/sabah-botu.git
   cd sabah-botu
   ```

2. Sanal ortamı oluştur ve kütüphaneleri kur:

   **Mac / Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   **Windows:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Telegram'da [@BotFather](https://t.me/BotFather) ile bir bot oluştur, token'ını al. Bota `/start` yazdıktan sonra chat ID'ni bul.

4. Proje klasöründe `.env` dosyası oluştur:
   ```
   TELEGRAM_TOKEN=senin_tokenin
   CHAT_ID=senin_chat_idn
   ```

5. Çalıştır:

   **Mac / Linux:**
   ```bash
   python3 bot.py
   ```

   **Windows:**
   ```powershell
   python bot.py
   ```

### Otomatik çalıştırma

GitHub'da repo ayarlarından **Settings → Secrets and variables → Actions** bölümüne `TELEGRAM_TOKEN` ve `CHAT_ID` değerlerini ekle. `.github/workflows/sabah.yml` dosyası botu her gün 06:00 UTC'de (09:00 Türkiye) çalıştırır. Actions sekmesinden **Run workflow** ile elle de çalıştırılabilir.

## Neler Öğrendim

- REST API'lere istek atmayı ve gelen JSON verisini Python sözlüğü olarak okumayı
- API dokümantasyonu okuyarak istek adreslerini kendim oluşturmayı
- Saat dilimlerinin (UTC ve yerel saat) veriyi nasıl etkilediğini
- Kodu fonksiyonlara ayırarak tekrar eden kısımları azaltmayı
- Token gibi gizli bilgileri `.env` dosyası ve GitHub Secrets ile güvenli şekilde saklamayı
- Git ve GitHub ile sürüm kontrolünü
- GitHub Actions ile bir işi zamanlanmış olarak otomatik çalıştırmayı (CI/CD temelleri)

