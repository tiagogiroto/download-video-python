import urllib.request
from urllib.parse import unquote
from tqdm import tqdm

url_links = ['']

for url_link in url_links:
    nome_video = url_link.split('/content/')[-1]
    nome_video = nome_video.split('/')
    nome_video = nome_video[1:]
    nome_video = unquote(nome_video[0])

    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=nome_video) as progress_bar:
        urllib.request.urlretrieve(url_link, nome_video, lambda block, block_size, total_size: progress_bar.update(block_size))

