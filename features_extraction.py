from bs4 import BeautifulSoup
import os
import futures as fe
import pandas as pd


# HTML dosyasini acip icerigi donduren fonskiyonu olustur

dosya = "mini_dataset/8.html"
def dosyayi_ac(dosya_adi):
    with open(dosya_adi,"r",encoding='utf-8') as f:
        return f.read()
# Beautifulsoup objesi olusturan fonksiyonu olustur
def soup_olustur(yazi):
    return BeautifulSoup(yazi,"html.parser")

# Vektor olusturan ve tum features icindeki fonksiyonlari calistiracak fonksiyonu olustur
def vektor_olustur(soup):
    return [
#        fe.baslik_kontrol(soup),
        fe.input_kontrol(soup),
        fe.buton_kontrol(soup),
        fe.resim_kontrol(soup),
        fe.submit_kontrol(soup),
        fe.link_kontrol(soup),
        fe.sifre_alani_kontrol(soup),
        fe.mail_alani_kontrol(soup),
        fe.gizli_etiket_kontrol(soup),
        fe.ses_dosyasi_kontrol(soup),
        fe.video_kontrol(soup),
        fe.input_sayisi(soup),
        fe.buton_sayisi(soup),
        fe.resim_sayisi(soup),
        fe.secenek_sayisi(soup),
        fe.liste_sayisi(soup),
        fe.TH_sayisi(soup),
        fe.TR_sayisi(soup),
        fe.href_sayisi(soup),
        fe.paragraf_sayisi(soup),
        fe.script_sayisi(soup),
        fe.baslik_uzunlugu(soup)
    ]


# 1, 2, 3 nolu adimlari her bir html dosyasi icin islet ve 2 boyutlu bir dizi elde et
klasor = "mini_dataset"
def iki_boyutlu_liste(klasor_adi):
    klasor_yolu = os.path.join(os.getcwd(), klasor_adi)
    veri = []
    for dosya in sorted(os.listdir(klasor_yolu)):
        yol= os.path.join(klasor_yolu,dosya)
        soup = soup_olustur(dosyayi_ac(yol))
        veri.append(vektor_olustur(soup))
    return veri

# 2 boyutlu dizi ile bir dataframe olustur
veri = iki_boyutlu_liste(klasor)

sutunlar = [
        # "baslik_kontrol",
        "input_kontrol",
        "buton_kontrol",
        "resim_kontrol",
        "submit_kontrol",
        "link_kontrol",
        "sifre_alani_kontrol",
        "mail_alani_kontrol",
        "gizli_etiket_kontrol",
        "ses_dosyasi_kontrol",
        "video_kontrol",
        "input_sayisi",
        "buton_sayisi",
        "resim_sayisi",
        "secenek_sayisi",
        "liste_sayisi",
        "TH_sayisi",
        "TR_sayisi",
        "href_sayisi",
        "paragraf_sayisi",
        "script_sayisi",
        "baslik_uzunlugu"

]

df = pd.DataFrame(data=veri, columns=sutunlar)
print(df.head(5))


