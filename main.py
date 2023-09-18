
# Download video 


import urllib.request
# pip install urllib3
from urllib.parse import unquote

url_links = ['','']

for url_link in url_links:
    
    nome_video = url_link.split('/content/')[-1] 
    nome_video = nome_video.split('/')
    nome_video = nome_video[1:]

    nome_video = unquote(nome_video[0])


    urllib.request.urlretrieve(url_link, nome_video) 


