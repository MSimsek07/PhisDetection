import streamlit as st
import machine_learning as ml
import url_expand as ue
import features_extraction as fe
from bs4 import BeautifulSoup
import requests as re
#import matplotlib.pyplot as plt

st.header("Phishing Url Tespit")


with st.expander("PROJEYE DAİR"):
    st.subheader("Yöntem")
    st.write("Bu projede aynı zamanda bir _makina öğrenmesi_ yöntemi de olan, _denetimli öğrenme_ aracılığıyla, bir urlin normal yasal bir site mi yoksa bir oltalama(phishing) yani zararlı mı olduğunu belli yüzdelerle tespit etmekte ve tahmin etmektedir.")
    st.write("Bu proje için kendi veri setimi kendim oluşturdum ve gerekli ağırlıkları - özellikleri veri setinden elde ettim. Tabii ki bunların bazıları kendi site tecrübelerim ve analizlerimden çoğunluğu da literatür ışığında oluşturuldu.")


    st.subheader("Veri Seti")
    st.write(' _"phishtank.org"_ & _"tranco-list.eu"_ sitelerinden gerekli olan urlleri temin ettim. ')

    etiketler = 'phishing', 'Normal/Zararsız'

    # ml.phishing_siteler_df = ml.phishing_siteler_df.drop('url', axis=1)
    # ml.phishing_siteler_df = ml.phishing_siteler_df.drop('baslik_kontrol', axis=1)
    # ml.phishing_siteler_df = ml.phishing_siteler_df.drop_duplicates()
    # ml.zararsizlar_df = ml.zararsizlar_df.drop('url', axis=1)
    # ml.zararsizlar_df = ml.zararsizlar_df.drop('baslik_kontrol', axis=1)
    # ml.zararsizlar_df = ml.zararsizlar_df.drop_duplicates()
    #
    # phishing_orani = int(ml.phishing_siteler_df.shape[0] / (ml.phishing_siteler_df.shape[0] + ml.zararsizlar_df.shape[0]))
    # normal_site_orani = 100 - phishing_orani
    # boyutlar = [phishing_orani, normal_site_orani]
    # bozulma = (0.1, 0)
    # fig, ax = plt.subplots()
    # ax.pie(boyutlar, explode=bozulma, labels=etiketler, shadow=True, startangle=90, autopct='%1.1f%%')
    # ax.axis('equal')
    # st.pyplot(fig)


    st.write("Özellikler + URL + etiket")

    st.markdown("etiket(label), 1 ise phishing | 0 ise normal-zararsız")
    sayi = st.slider("Satır numarası seçiniz", 0, 100)
    st.dataframe(ml.zararsizlar_df.head(sayi))

    @st.cache
    def data_frame_cevir(df):
        return df.to_csv().encode('utf-8')

    csv = data_frame_cevir(ml.df)
    st.download_button(
        label= "Veriyi csv olarak indiriniz",
        data=csv,
        file_name='phishing_zararsiz_islenmis_veri.csv',
        mime='text/csv'
    )
    st.subheader('Özellikler')
    st.write("Projede _content-based_ yani içerik tabanlı bir yöntem kullandım.")
    st.write("Özelliklerin bir çoğu Beautiful soup kütüphanesinin find_all() fonksiyonu kullanılarak elde edilen site deseni içerisinden ayıklanmıştır")

    st.subheader("Sonuç Olarak")
    st.write('Projeden bir kaç tane farklı makina öğrenmesi yapay zeka algoritması kullandım ve test ettim aralarından en öne çıkanları ise')
    st.write("""Mükemmel doğruluk(accuracy), duyarlılık(recall) ve hassasiyet(presicion) değeri ne olur?
            Doğruluk, bir sınıflandırıcının tüm göstergelerin doğruluğu veya yanlışlığı oranıdır. Mükemmel bir doğruluk değeri, 1 olur, yani tüm göstergelerin doğru tahmin edildiği anlamına gelir.
            Duyarlılık (recall), bir sınıflandırıcının pozitif göstergelerin doğruluğu veya yanlışlığı oranıdır. Mükemmel bir duyarlılık değeri, 1 olur, yani tüm pozitif göstergelerin doğru tahmin edildiği anlamına gelir.            
            Hassasiyet (precision), bir sınıflandırıcının pozitif tahminlerin doğruluğu veya yanlışlığı oranıdır. Mükemmel bir hassasiyet değeri, 1 olur, yani tüm pozitif tahminlerin doğru olduğu anlamına gelir.
            Ancak, genellikle mükemmel değerlerin her birini aynı anda elde etmek mümkün değildir. Bu nedenle, doğruluk, duyarlılık ve hassasiyet gibi ölçümler arasındaki dengeyi dikkate almak önemlidir. Örneğin, sınıflandırıcının duyarlılığı yüksek olabilir, ancak hassasiyeti düşük olabilir, veya tam tersi de olabilir. Hangisinin daha önemli olduğu, uygulamanın ihtiyaçlarına göre değişebilir.""")

    st.write("""Sınıflandırıcınızı eğittikten sonra, doğruluk, duyarlılık ve hassasiyet gibi ölçümleri kullanarak performansını değerlendirebilirsin. Doğruluk, bir sınıflandırıcının phishing URL'leri doğru bir şekilde tespit edip etmediğini ölçer. Duyarlılık, bir sınıflandırıcının phishing URL'lerini kaçırdığını ölçer. Hassasiyet, bir sınıflandırıcının pozitif tahminlerin doğruluğu veya yanlışlığı oranıdır. Hangisinin daha önemli olduğu, uygulamanızın ihtiyaçlarına göre değişebilir. Örneğin, bir banka için, duyarlılık daha önemli olabilir, çünkü phishing URL'lerini kaçırmak istemeyecektir. Ancak bir haber sitesi için, doğruluk daha önemli olabilir, çünkü yanlış pozitif tahminler kullanıcıların zamanını ve enerjisini boşa harcayabilir ve güvenilirliğini azaltabilir.""")

choice = st.selectbox("Lütfen bir makina öğrenmesi algoritması seçiniz",
                          [
                              'Gaussian Naive Bayes',
                              'Destek Vektör Makinesi',
                              'Karar Ağacı',
                              'Random Forest',
                              'AdaBoost',
                          ])

if choice == 'Gaussian Naive Bayes':
        model = ml.nb_model
        st.write('Gaussian Naive Bayes model seçildi!')
elif choice == 'Destek Vektör Makinesi':
        model = ml.svm_model
        st.write('Destek Vektör Makinesi modeli seçildi!')
elif choice == 'Karar Ağacı':
        model = ml.dt_model
        st.write('Karar Ağacı modeli seçildi!')
elif choice == 'Random Forest':
        model = ml.rf_model
        st.write('Random Forest model seçildi!')
else :
        model = ml.ab_model
        st.write("AdaBoost model seçildi!")


url = st.text_input('Url Giriniz : ')
url = ue.url_genislet(url)
if st.button("Kontrol Et"):
        try:
            response = re.get(url, verify=False, timeout=5)
            if response.status_code != 200:
                print("URL bağlantısı başarılı : ",url)
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                vektor = [fe.vektor_olustur(soup)]
                sonuc = model.predict(vektor)
                print(sonuc)
                if sonuc[0] == 0:

                    st.success("Bu URL ile ulaşacağınız site güvenilir gözüküyor!")
                    st.balloons()
                else:
                    st.warning("Dikkat! Bu web URL ile ulaşacağınız site potansiyel bir Phishingtir!")
                    st.snow()
        except re.exceptions.RequestException as e:
            print("___________", e)
