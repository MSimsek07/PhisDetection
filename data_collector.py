# veri toplama

import requests as re
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

from bs4 import BeautifulSoup
import pandas as pd
import features_extraction as fe

disable_warnings(InsecureRequestWarning)
URL_dosyasi = "C:\\Users\\muham\\GITHUB_REPOLAR\\PhisDetection\\top-1m.csv"
data_frame = pd.read_csv('top-1m.csv', names=["Index", "url"])
URL_dosyasi2 = "C:\\Users\\muham\\GITHUB_REPOLAR\\PhisDetection\\dogrulanmis_phishing_siteler.csv"
data_frame2 = pd.read_csv(URL_dosyasi2)





URL_listesi = data_frame['url'].to_list()
URL_listesi2 = data_frame2['url'].to_list()

baslangic = 0
bitis =16000

baslangic2 = 0
bitis2 = 10000

liste = URL_listesi[baslangic:bitis]
liste2 = URL_listesi2[baslangic2:bitis2]

https_etiketi = "http://"
liste = [https_etiketi + str(url) for url in liste]

def yapilandirilmis_veri_olustur(url_listesi):
    veri_listesi = []
    for i in range(0, len(url_listesi)):
        try:
            response = re.get(url_listesi[i], verify=False, timeout=5)
            if response.status_code != 200:
                print(i," Url için HTTP baglantisi basarili : ", url_listesi[i])
            else:

                soup = BeautifulSoup(response.content,"html.parser")
                vektor = fe.vektor_olustur(soup)
                vektor.append(str(url_listesi[i]))
                veri_listesi.append(vektor)
        except re.exceptions.RequestException as e:
            print(i," Hata =====> ",e)
            continue
    return veri_listesi

veri = yapilandirilmis_veri_olustur(liste)
veri2 = yapilandirilmis_veri_olustur(liste2)

sutunlar = [
    'baslik_kontrol',
    'input_kontrol',
    'buton_kontrol',
    'resim_kontrol',
    'submit_kontrol',
    'link_kontrol',
    'sifre_alani_kontrol',
    'mail_alani_kontrol',
    'gizli_etiket_kontrol',
    'ses_dosyasi_kontrol',
    'video_kontrol',
    'input_sayisi',
    'buton_sayisi',
    'resim_sayisi',
    'secenek_sayisi',
    'liste_sayisi',
    'TH_sayisi',
    'TR_sayisi',
    'href_sayisi',
    'paragraf_sayisi',
    'script_sayisi',
    'baslik_uzunlugu',
    'url'
]

df = pd.DataFrame(data=veri, columns=sutunlar)
df2 = pd.DataFrame(data=veri2, columns=sutunlar)

# etiketleme
df['label'] = 0
df2['label'] = 1

df.to_csv("yapilandirilmis_zararsiz_site_verileri.csv", mode='a', index=False)
df2.to_csv("yapilandirilmis_phishing_site_verileri.csv", mode='a', index=False)
