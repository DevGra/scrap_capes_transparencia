from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver as wbw # Import from seleniumwire
from time import sleep

#from selenium.webdriver import Chrome
import requests
import json
import urllib
import csv

base_url = 'http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces'
'''
browser = webdriver.Chrome()
browser.get(base_url)
#browser.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a').click()
link = browser.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
wait = WebDriverWait(link, 5)
link.click()
'''
d_wire = wbw.Chrome()
pg = d_wire.get(base_url)
WebDriverWait(pg, 2)
link = d_wire.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
link.click()
# import pdb; pdb.set_trace()
WebDriverWait(d_wire, 6)
print("executando o refresh.........")
d_wire.refresh()
print("Executou o reflesh!")
WebDriverWait(d_wire, 3)
import pdb;pdb.set_trace()
#img_cod = d_wire.execute_async_script('var ajax = new XMLHttpRequest(); ajax.open("GET", "http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=*", true); ajax.send(); ajax.onreadystatechange = function() { if (ajax.readyState == 4 && ajax.status == 200) { var data = ajax.responseText; console.log(data); return data;}}')
img_cod = d_wire.execute_async_script()

#d_wire.execute_async_script(script= "ajax.js")
import pdb; pdb.set_trace()
ajax_url = 'http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=*'
v = d_wire.execute_script('var date = new Date(); date.getTime();')
codigo = v
data_ajax = {'v': codigo }
customHead = {
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.3.92766818.1572461530; _gid=GA1.3.369187979.1572461530; JSESSIONID=wdnweolwqz2M18JBFkPl_8K9r3CATwpC3nuxa7a3.idc-jboss2-ap3-p",
    "Host": "www.portaltransparencia.gov.br",
    "Referer": "http://www.portaltransparencia.gov.br/servidores/consulta?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=detalhar%2Ctipo%2Ccpf%2Cnome%2CorgaoServidorExercicio%2CorgaoServidorLotacao%2Cmatricula%2CtipoVinculo%2Cfuncao&orgaosServidorExercicio=OR70000&tipo=2&ordenarPor=nome&direcao=asc",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}



pgf = requests.get('http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=*')
#req = pgf.requests
import pdb; pdb.set_trace()
sleep(1)
select_anos = Select(d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]'))
WebDriverWait(d_wire, 2)
select_anos.select_by_index(1)
#select_anos.click()

WebDriverWait(d_wire, 2)
# select_ano = d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]/option[2]')
# select_ano.click()
# WebDriverWait(d_wire, 1)

select_ufs = d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]')
select_ufs.click()
WebDriverWait(pg, 3)
select_uf = d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]/option[2]')
select_uf.click()
WebDriverWait(d_wire, 1)
select_institus = d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]')
select_institus.click()
WebDriverWait(pg, 3)
select_institu = d_wire.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]/option[2]')
select_institu.click()
WebDriverWait(d_wire, 1)
import pdb; pdb.set_trace()
captcha_click = d_wire.find_element_by_id('imgCaptcha').click()
d_wire.execute_async_script(script= "ajax.js")
captcha = captcha_click.text

print("Pare aqui")
import pdb; pdb.set_trace()




pg = requests.get(base_url)
import pdb; pdb.set_trace()
pg_face = 'http://transparencia.capes.gov.br/transparencia/xhtml/index.faces'
pgf = requests.get(pg_face)
import pdb; pdb.set_trace()                                                              #1575407977421
#base_captcha = 'http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=1575401704608'
base_captcha = 'http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=*'
pgc = requests.get(base_captcha)
header = pgc.headers['Set-Cookie']
extraindo_captcha = header.split(',')[1]
cod_txt = extraindo_captcha.split('=')[1]
cod = int(cod_txt)
import pdb; pdb.set_trace()
anos = list(range(1994, 2020))
estados = list('AC','AL','AM','BA','CE','DF','ES','GO','MG','MT','NA','PA','PB','PE','PI','PR','RJ','RN','RO','RS','SC','SP','ZZ')
'''
code javascript para inserir o captcha no SELENIUM
document.getElementById("formularioPesquisa:validacaoImagem").value = 69911;
'''
