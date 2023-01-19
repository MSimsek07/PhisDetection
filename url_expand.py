import urlexpander
import re
#url = "http://shorturl.at/muCT4"

def url_emin_ol(url):
    try:
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        match = re.search(url_pattern, url)
        if match:
            return False
        return True

    except Exception as e:
        print(e)


def url_genislet(url):
    try:
        if url_emin_ol(url) == False:
            print('Girilen URL kısaltılmış URldir')
            expandend_url = urlexpander.expand(url)
            url = expandend_url
            print(url)
            return url
        else:
            print('Girilen URL normaldir')
            return url
    except Exception as e:
        print(e)
#url_genislet(url)