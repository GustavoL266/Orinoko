"""Auditoria estática sem dependências: python scripts/verify.py."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs
import json
import re

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets, self.images = [], [], [], []
        self.h1 = 0
        self.lang = None
        self.iframe_titles = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'h1':
            self.h1 += 1
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'iframe':
            self.iframe_titles.append(attrs.get('title'))
        if tag == 'script' and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon'):
            self.assets.append(attrs['href'])


html = (ROOT / 'index.html').read_text(encoding='utf-8')
page = Page()
page.feed(html)
assert page.lang == 'pt-BR'
assert page.h1 == 1
assert len(page.ids) == len(set(page.ids)), 'IDs duplicados'
assert all(page.iframe_titles), 'Mapa sem título'
assert not page.images, 'Rever autorização e origem de qualquer fotografia'
for href in page.links:
    assert href, 'Link vazio'
    if href.startswith('#'):
        assert href[1:] in page.ids, f'Âncora ausente: {href}'
for asset in page.assets:
    assert (ROOT / asset).is_file(), f'Asset ausente: {asset}'
whatsapp = [href for href in page.links if 'wa.me' in href]
assert len(whatsapp) >= 4
for href in whatsapp:
    parsed = urlparse(href)
    assert parsed.netloc == 'wa.me' and parsed.path == '/5519974111822'
    assert parse_qs(parsed.query)['text'][0] == 'Olá! Vim pelo site da Padaria Orinoko e gostaria de mais informações.'
maps = [href for href in page.links if 'google.com/maps?' in href]
assert maps and all(parse_qs(urlparse(href).query)['cid'] == ['2691141686588367925'] for href in maps)
schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))
assert schema['@type'] == 'Bakery'
assert schema['telephone'] == '+55-19-97411-1822'
assert 'aggregateRating' not in schema  # Avoid self-serving review structured data.
assert 'og:image' not in html
assert 'prefers-reduced-motion' in (ROOT / 'css/style.css').read_text(encoding='utf-8')
assert ':focus-visible' in (ROOT / 'css/style.css').read_text(encoding='utf-8')
assert 'instagram.com' not in html
assert not re.search(r'unsplash|pexels|pixabay|pinterest|data:image/(png|jpeg)', html, re.I)
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for target in re.findall(r'\]\((\./[^)]+)\)', readme):
    assert (ROOT / unquote(target)).exists(), f'Link do README ausente: {target}'
print(f'PASS: {len(page.links)} links, {len(page.assets)} assets, {len(whatsapp)} links WhatsApp, JSON-LD, âncoras, origem das imagens e links locais do README.')
