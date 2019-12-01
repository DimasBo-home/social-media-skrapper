# https://m.facebook.com/search/posts/?q=фудбол&source=filter&isTrending=0
import requests
from bs4 import BeautifulSoup

url = "https://m.facebook.com/search/posts/?q={question}&source=filter&isTrending=0".format(question="фудбол")

headers = ({
'Host': 'm.facebook.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': 'sb=E6WDXXJVHdLlw5P_AFKn-413; datr=E6WDXYScBiaVONSBkupJHo7_; c_user=100010887617912; xs=46%3AI_Huxs56T_37Gw%3A2%3A1568908597%3A20807%3A15696; fr=3pRPonbwnP00n373i.AWXX9cN5pzgfEHAvW2vYwmr7Nng.Bdg6U0.3e.F2W.0.0.Bd3ayb.; spin=r.1001474306_b.trunk_t.1574808735_s.1_v.2_; noscript=1',
'Upgrade-Insecure-Requests': '1',
'TE': 'Trailers',
})

params = {

}

r = requests.get(url,headers=headers)
print(r)
print(url)
s = BeautifulSoup(r.text,'lxml')
context = s.body

with open("facebook_search.html","w") as f:
    f.write(str(context))