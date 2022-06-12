import requests
import json
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup


def search_data(id):
    ACCESS_TOKEN = 'IqFKRu8PXcFn3uDE6nvHX5GDtL5fEAoezJgBnM66cgUf6SlT2RcFBp6ROtQN'
    url = 'https://zenodo.org/api/records/'+id
    r = requests.get(url,
                     params={'access_token': ACCESS_TOKEN})
    js =  r.json()

    def values(val):
      if val != None:
        return True
      return False

    js = r.json()
    md = js['metadata']
    f1 = values(js['doi'])
    f21 = values(md['creators'])
    f22 = values(md['title'])
    f23 = values(md['publication_date'])
    f24 = values(re.sub(r'\<[^>]*\>', '', md['description']))
    try:
      f25 = values(md['keywords'])
    except:
      f25 = False
    f26 = values(js['owners'])
    a1 = values(md['access_right'])
    i3 =  values(js['links'])
    r12 = values(js['created'])

    r1 = False
    try:
        links_to_files = [i['links']['self'] for i in js['files']]
        if len(links_to_files)>0: r1 = True
    except:
        pass

    try:
      list_communities = [i['id'] for i in md['communities']]
      r13 = True
    except:
      r13 = False



    def find_license(text):
      t = requests.get(text).text
      soup = BeautifulSoup(t, features='html.parser')
      lic = soup.find('a', attrs={'rel':'license'})
      return lic.text


    def f3():
      if js['doi'] == md['doi']:
        return True
      return False

    r11 = values(find_license(js['links']['html']))

    f = [f1, f21, f22, f23, f24, f25, f26, f3()]
    a = [a1]
    i = [i3]
    rr = [r1, r11, r12, r13]
    f0 = sum(f) / len(f) * 0.25
    a0 = sum(a) / len(a) * 0.25
    i0 = sum(i) / len(i) * 0.25
    r0 = sum(rr) / len(rr) * 0.25
    overall = sum([f0, a0, i0, r0]) * 100
    dict = {}
    dict['title'] = js['metadata']['title']
    dict['fairness'] = overall
    dict['f1'] = f1
    dict['f21'] = f21
    dict['f22'] = f22
    dict['f23'] = f23
    dict['f24'] = f24
    dict['f25'] = f25
    dict['f26'] = f26
    dict['f3'] = f3()
    dict['a1'] = a1
    dict['i3'] = i3
    dict['r1'] = r1
    dict['r11'] = r11
    dict['r12'] = r12
    dict['r13'] = r13
    return dict