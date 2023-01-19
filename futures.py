from bs4 import BeautifulSoup

with open("mini_dataset/8.html") as f:
    deneme = f.read()


soup = BeautifulSoup(deneme,"html.parser")

#kotrol edilecek binari icerikler

#baslik_kontrol
def baslik_kontrol(soup):
    try:
        if len(soup.tite.text) > 0:
            return 1
        else:
            return 0
    except BaseException:
        print(BaseException)

# input_kontrol
def input_kontrol(soup):
    if len(soup.find_all("input")) > 0:
        return 1
    else:
        return 0
# buton_kontrol
def buton_kontrol(soup):
    if len(soup.find_all("button")) > 0:
        return 1
    else:
        return 0
# resim_kontrol
def resim_kontrol(soup):
    if len(soup.find_all("image")) == 0:
        return 0
    else:
        return 1
# submit_kontrol
def submit_kontrol(soup):
    for button in soup.find_all("input"):
        if button.get("type") == "submit":
            return 1
        else:
            pass
    return 0
# link_kontrol
def link_kontrol(soup):
    if len(soup.find_all("link")) > 0:
        return 1
    else:
        return 0
# sifre_alani_kontrol
def sifre_alani_kontrol(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("name") or input.get("id")) == "password":
            return 1
        else:
            pass
    return 0



# mail_alani_kontrol
def mail_alani_kontrol(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("name") or input.get("id")) == "email":
            return 1
        else:
            pass
    return 0
# gizli_etiket_kontrol
def gizli_etiket_kontrol(soup):
    for input in soup.find_all("input"):
        if input.get("type") == "hidden":
            return 1
        else:
            pass
    return 0
# ses_dosyasi_kontrol
def ses_dosyasi_kontrol(soup):
    if len(soup.find_all("audio")) > 0:
        return 1
    else:
        return 0

# video_kontrol
def video_kontrol(soup):
    if len(soup.find_all("video")) > 0:
        return 1
    else:
        return 0

#================================ Binari Olmayanlar ==================================
# input_sayisi
def input_sayisi(soup):
    return len(soup.find_all("input"))
# buton_sayisi
def buton_sayisi(soup):
    return len(soup.find_all("button"))
# resim_sayisi
def resim_sayisi(soup):
    resim_taglari = len(soup.find_all("images"))
    sayac = 0
    for meta in soup.find_all("meta"):
        if meta.get("type") or meta.get("name") == "image":
            sayac+=1
    return resim_taglari + sayac

# secenek_sayisi
def secenek_sayisi(soup):
    return len(soup.find_all("option"))
# liste_sayisi
def liste_sayisi(soup):
    return len(soup.find_all("li"))
# TH_sayisi
def TH_sayisi(soup):
    return len(soup.find_all("th"))
# TR_sayisi
def TR_sayisi(soup):
    return len(soup.find_all("tr"))
# href_sayisi
def href_sayisi(soup):
    sayac = 0
    for link in soup.find_all("link"):
        if link.get("href"):
            sayac+=1
    return sayac

# paragraf_sayisi
def paragraf_sayisi(soup):
    return len(soup.find_all("p"))
# script_sayisi
def script_sayisi(soup):
    return len(soup.find_all("script"))
# baslik_sayisi
def baslik_uzunlugu(soup):
    if soup.title is not None:
        # Access the text attribute of the title element
        baslik = soup.title.text
    else:
        # Set the title text to an empty string
        baslik = ""
    return len(baslik)

print("baslik_kontrol --> ", baslik_kontrol(soup))
print("input_kontrol --> ", input_kontrol(soup))
print("buton_sayisi --> ", buton_sayisi(soup))
print("resim_kontrol --> ", resim_kontrol(soup))
print("submit_kontrol --> ", submit_kontrol(soup))
print("link_kontrol --> ", link_kontrol(soup))
print("sifre_alani_kontrol --> ", sifre_alani_kontrol(soup))
print("mail_alani_kontrol --> ", mail_alani_kontrol(soup))
print("gizli_etiket_kontrol --> ", gizli_etiket_kontrol(soup))
print("ses_dosyasi_kontrol --> ", ses_dosyasi_kontrol(soup))
print("video_kontrol --> ", video_kontrol(soup))

print("input_sayisi --> ", input_sayisi(soup))
print("buton_sayisi --> ", buton_sayisi(soup))
print("resim_sayisi --> ", resim_sayisi(soup))
print("secenek_sayisi --> ", secenek_sayisi(soup))
print("liste_sayisi --> ", liste_sayisi(soup))
print("TH_sayisi --> ", TH_sayisi(soup))
print("TR_sayisi --> ", TR_sayisi(soup))
print("href_sayisi --> ", href_sayisi(soup))
print("paragraf_sayisi --> ", paragraf_sayisi(soup))
print("script_sayisi --> ", script_sayisi(soup))
print("baslik_uzunlugu --> ", baslik_uzunlugu(soup))