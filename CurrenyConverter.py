import requests
import pandas as pd

def get_supported_currencies(api_key):
        
   #API'den desteklenen tüm para birimlerinin kısaltmalarını alır.

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/codes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["supported_codes"]
    else:
        return "Desteklenen para birimleri alınırken hata oluştu."

def get_exchange_rate(api_key, from_currency, to_currency):
    
    #Verilen döviz çifti için döviz kurunu alır.

    
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["conversion_rate"]
    else:
        return "Döviz kuru alınırken hata oluştu."
        

def convert_currency(api_key, from_currency, to_currency, amount):
    
    #Girilen miktarı istenilen dövize çevirir.
        
    rate = get_exchange_rate(api_key, from_currency, to_currency)
    if isinstance(rate, float):
        converted_amount = amount * rate
        return converted_amount
    else:
        return rate

api_key = ("3770a4ec37fd2a7b71f5d654")
currencies = get_supported_currencies(api_key)   

pd.set_option('display.max_rows', None) 
    
if isinstance(currencies, list):
    # Para birimlerini tablo halinde gösterme
    df = pd.DataFrame(currencies, columns=['Kısaltma', 'Para Birimi Adı'])
    print("Desteklenen Para Birimleri:")
    print(df)    

# Kullanıcıdan veri alma

from_currency = input("Çevirmek istediğiniz para birimi (örneğin TRY): ").upper()
to_currency = input("Hangi para birimine çevirmek istiyorsunuz (örneğin USD): ").upper()
amount = float(input("Çevrilecek miktar: "))

# Döviz çevirme işlemi
converted_amount = convert_currency(api_key, from_currency, to_currency, amount)

if isinstance(converted_amount, float):
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print(converted_amount)