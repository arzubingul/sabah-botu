import requests
import os 
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN") 
chat_id = os.getenv("CHAT_ID") 

# 1 sıcaklık
def hava_durumu_getir():

    url = "https://api.open-meteo.com/v1/forecast?latitude=40.755&longitude=30.3934&current=temperature_2m&timezone=auto&forecast_days=1"
    cevap = requests.get(url) # get fonks. adrese gidip cevabı getiriyor
    veri = cevap.json() # cevabı(json ı) python sözlüğüne çevirme

    return veri["current"]["temperature_2m"]

# 2 dolar ve euro
def kur_getir(para_birimi):

    url = f"https://api.frankfurter.dev/v1/latest?base={para_birimi}&symbols=TRY"
    cevap = requests.get(url)
    veri = cevap.json()

    return veri["rates"]["TRY"]

# 3 altın
def altin_getir():

    url = "https://api.frankfurter.dev/v2/rate/XAU/TRY"
    cevap = requests.get(url)
    veri = cevap.json()

    ons_fiyat = veri["rate"]
    gram_fiyat = ons_fiyat / 31.1034768 # 1 troy ons kaç gram (altın fiyatını grama çevirmek için)

    return  gram_fiyat

def mesaj_gonder(metin):

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    parametreler = {
        "chat_id": chat_id,
        "text": metin
    }
    requests.post(url, data=parametreler)

sicaklik = hava_durumu_getir()
dolar = kur_getir("USD")
euro = kur_getir("EUR")
altin = altin_getir()

mesaj = f"Günaydın :)\n\nSıcaklık: {sicaklik} °C\nDolar: {dolar:.2f} TL\nEuro: {euro:.2f} TL\nAltın: {altin:.2f} TL"

mesaj_gonder(mesaj)


