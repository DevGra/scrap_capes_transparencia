
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
pg = driver.get('http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces')
link = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
link.click()

WebDriverWait(driver, 4)
anos = driver.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]')
anos.click()
WebDriverWait(driver, 2)
ano = driver.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]/option[2]')
ano.click()
WebDriverWait(driver, 3)
#import pdb; pdb.set_trace()
ufs = driver.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]')
ufs.click()
WebDriverWait(driver, 2)
uf = driver.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]/option[2]')
uf.click()
WebDriverWait(driver, 2)
insts = driver.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]')
insts.click()
WebDriverWait(driver, 1)
inst = driver.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]/option[2]')
inst.click()