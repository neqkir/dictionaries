# neqkir

# get the vocabulary in CNRTL - Le Tresor de la Langue Francaise Informatise 

import os
import sys
import urllib
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup
import requests
import string

dictionary = []

def get_words_in_page( url ):
    #print( url )
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "lxml")
    lst = ""
    for w in soup.findAll("a",{"href":regex}):
        dictionary.append(w.string)
        lst=w.string
    #print(lst)

base_url = "https://www.cnrtl.fr/portailindex/LEXI/TLFI/"

for l in string.ascii_lowercase:
    base_url = base_url + l.upper()    
    get_words_in_page( base_url )
    
    next_index = 0

    while True:
        next_index += 80
        url = base_url+"/"+str(next_index)   
        try:
            res = urllib.request.urlopen(url)
        except ValueError:
            break

        get_words_in_page( url )
