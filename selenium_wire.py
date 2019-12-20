from seleniumwire import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pprint import pprint as show


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

driver = webdriver.Chrome(chrome_options=options)

pg = driver.get('http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces')
link = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
link.click()
sleep(3)
#driver.refresh()
'''
count_ano = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="formularioPesquisa:anoConsulta"]/option'))))
print(str(count_ano) + " items.")
dropdown_ano = Select(driver.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]'))

a = 2 # iteravel de ano - começa em 1994(segundo item do dropdown)
for op_a in dropdown_ano.options:
    ano = op_a.get_attribute('innerHTML')
    if ano != "Selecione...":
        print(str(a) + " - " + ano)
        #--------------------------------- ANOS ---------------------------------------------------------
        dropdown_anos = driver.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]/option[1]')
        dropdown_anos.click()
        WebDriverWait(driver, 2)
        ano = driver.find_element_by_xpath('//*[@id="formularioPesquisa:anoConsulta"]/option['+ str(a) + ']')
        ano.click()
        WebDriverWait(driver, 3)
        sleep(1)
        #import pdb; pdb.set_trace()
        #------------------------------- UF ---------------------------------------------------------------
        #driver.wait_for_request(path = '/transparencia/xhtml', timeout = 30)
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="formularioPesquisa:anoConsulta"]/option')))
            dropdown_ufs = Select(driver.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]'))
        except Exception as e:
            print("Ainda não carregou os estados...", e)

        u = 2
        for op_uf in dropdown_ufs.options:
            uf = op_uf.get_attribute('innerHTML')
            if uf != "Selecione...":
                print(str(u) + " - " + uf)
                uf = driver.find_element_by_xpath('//*[@id="formularioPesquisa:ufConsulta"]/option['+ str(u) + ']')
                uf.click()
                sleep(1)
                #------------------------------- Instituicao--------------------------------------------------------------
                try:
                    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]/option')))
                    dropdown_inst = Select(driver.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]'))
                except Exception as e:
                    print("Ainda não carregou as Instituições...", e)
                i = 2
                for op_inst in dropdown_inst.options:
                    institu = op_inst.get_attribute('innerHTML')
                    if institu != "Selecione...":
                        print(str(i) + " - " + institu)
                        inst = driver.find_element_by_xpath('//*[@id="formularioPesquisa:idEntidadeEnsinoConsulta"]/option['+ str(i) + ']')
                        inst.click()
                        sleep(1)
                        i += 1
                #--------------------------------- FIM INSTITUICAO ------------------------------------------------------
                u += 1
                #import pdb; pdb.set_trace()
                sleep(1)
        print("Outro ano...")
        a += 1

    if a == 2:
        print("Passou o primeiro loop...")
    print("O valor de a eh: ", a)
    #import pdb; pdb.set_trace()
'''
code_javascript = 'var date = new Date(); \
    return "http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=" + date.getTime();'

pg_img = 'function reloadImgCaptcha(id) { \
	      var obj = document.getElementById(id); \
	      var src = obj.src; \
	      var pos = src.indexOf("?"); \
    	if (pos >= 0) {   \
    		src = src.substr(0, pos); \
    	} \
	       var date = new Date(); \
	return obj.src = src + "?v=" + date.getTime(); \
    }\
    img = reloadImgCaptcha("imgCaptcha"); \
    async function fetchAsync (img) { \
    let response = await fetch(img); \
    let data = await response.json(); \
    return {data} \
    } '
pg_img = driver.execute_script(script=pg_img)
import pdb; pdb.set_trace()
cookies = driver.get_cookies()
session = requests.Session()
#driver.wait_for_request(path="/transparencia/xhtml", timeout=5)
print("Reload....")
sleep(3)
#session_url = driver.command_executor._url
#session_id = driver.session_id
show(driver.session_id)
import pdb; pdb.set_trace()
cod = driver.refresh(driver.execute_script(script=code_javascript))

#sleep(4)
#driver.implicitly_wait(30)
#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("r").perform()
print('fim do reload')
sleep(2)
import pdb; pdb.set_trace()
cks = driver.get_cookies()
req = driver.requests
#cook = driver.get_cookie()
import pdb; pdb.set_trace()
request_ajax_img = driver.wait_for_request('http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v='+str(driver.execute_script(script=code_javascript)),timeout=20)
