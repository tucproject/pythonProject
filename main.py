import requests
import json

def search_zenodo(search_query):
    ACCESS_TOKEN = 'IqFKRu8PXcFn3uDE6nvHX5GDtL5fEAoezJgBnM66cgUf6SlT2RcFBp6ROtQN'
    r = requests.get('https://zenodo.org/api/records',
                     params={'q': search_query,
                              'type': 'dataset',
                             'accessrights': 'open',
                             'filetype': 'csv',
                             'access_token': ACCESS_TOKEN})
    js = r.json()
    print(js['links'])
    for i in js['links']:
        print(i)
    n = js['hits']['hits']
    return [j['conceptrecid'] for j in n]