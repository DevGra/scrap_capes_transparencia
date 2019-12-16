import pdb

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver as wbw # Import from seleniumwire
from time import sleep
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

# from selenium.webdriver import Chrome
import requests
import json
import urllib
import csv

base_url = 'http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces'
# session = HTMLSession()
# r = session.get(base_url)
# import pdb; pdb.set_trace()
# assincrono
session = AsyncHTMLSession()


async def get_pythonorg():
    r = await session.get('http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces')
    return r

func = get_pythonorg
import pdb; pdb.set_trace()
result = session.run(get_pythonorg)
import pdb; pdb.set_trace()
