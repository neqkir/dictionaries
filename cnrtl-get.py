# neqkir

# get the vocabulary in CNRTL - Le Tresor de la Langue Francaise Informatise 

import os
import re
import sys
import time
import urllib
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup
import requests
import tqdm
import string

dictionary = []

regex = re.compile("/definition/*")

def get_words_in_page( url ):
    print( url )
    words=[]
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "lxml")
    lst = ""
    for w in soup.findAll("a",{"href":regex}):
        words.append(w.string)
    print(words[-1])

    return words

base_url = "https://www.cnrtl.fr/portailindex/LEXI/TLFI/"

for l in string.ascii_lowercase:
    
    base_url_letter = base_url + l.upper()    
    dictionary += get_words_in_page( base_url_letter )
    
    next_index = 0

    while True:

        next_index += 80
        url = base_url_letter+"/"+str(next_index)

        words = get_words_in_page( url )
        if words == ["Lexicographie"]:
            break
        else:
            dictionary += words

all_words='\n'.join('{}'.format(item) for item in dictionary)
with open(os.path.join("cnrtl-dictionary.txt"), "w", encoding="utf8") as file:
    file.write(all_words)
