import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO SITE DO PUDIM NÃO ESTA ACESSIVEL NO MOMENTO\033[m')
else:
    print('\033[32mO SITE DO PUDIM ESTA ACESSIVEL\033[m')
