import requests
from bs4 import BeautifulSoup

def getForms():
    url = 'http://www.wh26.tu-dresden.de/index.php?main=userlounge&sub=settings'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    sel = soup.find('select')
    o = sel.find('option')
    forms = []
    while(o != None):
        forms.append(o.attrs['value'])
        o = o.find('option')
    return forms

def getIp(form):
    return form.split(';')[2]

def getMac(form):
    url = 'http://www.wh26.tu-dresden.de/index.php?main=userlounge&sub=settings'
    data = {
        'authuserroom':form,
        'authtype':'room',
        'authpw':'ok'}
    r = requests.post(url, data)
    soup = BeautifulSoup(r.text)
    return soup.find(attrs={'name':'mac'}).attrs['value']

def getIpMacs():
    forms = getForms()
    res = []
    for f in forms:
        try:
            i = getIp(f)
            m = getMac(f)
            res.append((i,m))
        except Exception:
            pass
    return res

