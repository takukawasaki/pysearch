#!/usr/local/bin/python3

import urllib.request,urllib.error,urllib.parse
from bs4 import *

appid = "dj0zaiZpPW5ySEZQZ096cUNJbyZzPWNvbnN1bWVyc2VjcmV0Jng9NmI-"
pageurl =" http://jlp.yahooapis.jp/MAService/V1/parse"

def split(sentence,appid = appid, results = "ma",filter="1|2|4|5|9|10"):
    ret =[]
    sentence = urllib.parse.quote_plus(sentence.encode("utf-8"))
    query ="%s?appid=%s&results=%s&uniq_filter=%s&sentence=%s" % \
      (pageurl,appid,results, filter ,sentence)
    soup =BeautifulSoup(urllib.request.urlopen(query))
    try:
        return [l.surface.string for l in soup.ma_result.word_list]
    except:return[]
