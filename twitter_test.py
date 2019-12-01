import requests
from bs4 import BeautifulSoup

# headers = (
#     {'User-Agent':
#          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
#      })
url = "https://mobile.twitter.com/search?q={question}&s=typd&lang={lang}".format(question="фудбол",lang="uk")
headers = ({
"Host": "mobile.twitter.com",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
'Connection': "keep-alive",
'Cookie': 'personalization_id="v1_/14v3F7e9RUPNA44QWb2cw=="; guest_id=v1%3A157480633581299386; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; ct0=82c6674285d46852641df9a1e1dbfa56; _ga=GA1.2.1340694208.1574806344; _gid=GA1.2.982443787.1574806344; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFCxxaluAToMY3NyZl9p%250AZCIlOWZlZWY2ZTQ4MDlkNzc2NTA2OWNhMWQxNmVmNzFhNjQ6B2lkIiUxNGRh%250ANTlhOWQ2YzQ1ZDViNTEyMTEwNmMxOWU1MzU0Mg%253D%253D--d280dcb84446af7caa25007b1d2a6b18c32b39fc; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iLThjM2E1NzhkZmZkZjAzNjNlMDNhMDIwZjU2ZTE3ZGViZTJlNGM5YmI%3D--f65c6cd3be47af83fb1e7866adc1f6f7881714aa; m5=off; mobile_metrics_token=157480773627379596; lang=uk; d=32',
'Upgrade-Insecure-Requests': '1',
'TE': 'Trailers'
})
params = {

}
r = requests.get(url,headers=headers)
print(r)
print(url)
s = BeautifulSoup(r.text,'lxml')
context = s.body
with open("twiter_search.html","w",encoding="utf-8") as f:
    f.write(str(context))