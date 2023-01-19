import requests as re
from bs4 import BeautifulSoup
import os
url = "https://www.kaggle.com"
response = re.get(url)

print("response ===> ", response, " \n ", type(response))
print("Bilgi ===> ", response.text, "  ", "\nicerik ===> ", response.content, "  ", " durum ===> ", response.status_code)

if response.status_code != 200:
    print("Baglanti basarisiz")
else:
    print("Baglanti basarili")

soup = BeautifulSoup(response.content, "html.parser")

print("Baslik etiketli ===> ",soup.title, "\ntitle etiketsiz ===> ", soup.title.text)

for link in soup.findAll("link"):
    print(link.get("href"))

print(soup.get_text())

# HTML dosyalarını saklamak için bir klasör oluştur
klasor = "mini_dataset"
if not os.path.exists(klasor):
    os.mkdir(klasor)

# Veri kazıyan ve return eden fonksiyonu tanımla
def icerik_kazi(url):
    response = re.get(url)
    if response.status_code == 200:
        print("HTTP baglantisi basarili URL: ", url)
        return response
    else:
        print("HTTP baglantisi basarisiz  URL: ", url)
        return None
# Dizine HTML dosyasını kaydetmek için fonksiyonu tanımla
dosya_yolu = os.getcwd() + "/" + klasor
def html_kaydet(nereye, yazi, isim):
    dosya_adi = isim + ".html"
    with open(os.path.join(nereye, dosya_adi),"w",encoding='utf-8') as f:
        f.write(yazi)
deneme_yazi = response.text
html_kaydet(dosya_yolu,deneme_yazi, "deneme")

# URL listesi değişkeni tanımla
url_list =[
    "https://www.kaggle.com",
    "https://medium.com/",
    "https://tr.wikipedia.org/wiki/Medium",
    "https://medium.com/t%C3%BCrkiye",
    "https://www.medicalmedium.com/",
    "https://www.medicalmedium.com/",
    "https://eliciamiller.com/medicalmedium/",
    "https://www.charlottewiering.nl/shop",
    "https://www.facebook.com/groups/255003835572279/"
]
# URL listesini alan ve 2. adımı çalıştıran her bir URL için 3. adımı tekrarlayan fonksiyonu tanımla

def mini_bir_veriseti_yap(nereye, url_list):
    for i in range(0, len(url_list)):
        icerik = icerik_kazi(url_list[i])
        if icerik is not None:
            html_kaydet(nereye,icerik.text,str(i))
        else:
            pass
    print("mini dataset olusturuldu !")

mini_bir_veriseti_yap(dosya_yolu, url_list)
# 10 tane farklı HTML dosyası var mı kontrol et



