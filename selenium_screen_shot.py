from selenium import webdriver #For Selenium Web Driver
import os #For executing terminal commands as well as accessing directory
import requests #For Session
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytesseract as ocr # para reconhecimento de captcha atraves da imagem
from PIL import Image # para tratamento de imagem

# --------  acessando a pagina principal --------------
url_main = "http://transparencia.capes.gov.br/transparencia/xhtml/index.faces" #Target Url
browser = webdriver.Chrome() #Loading Browser Instance
browser.get(url_main) #Opening Target Url
link = browser.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
link.click()
sleep(3)

#---------- acessando a página de seleção do ano, estado, instituição ----------
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
                        # ------------------ tira um print da pagina --------------------------
                        browser.save_screenshot("pg_main.tif")
                        # ----- lendo a imagem e recortando o captcha -----
                        img = Image.open(r"pg_main.tif")# abrindo a screenshot salva
                        # import pdb; pdb.set_trace()
                        border = (366, 585, 615, 660) # left, up, right, bottom - selecionando a imagem
                        cropped_img = img.crop(border)# cortando apenas o tamanho do captcha
                        # import pdb; pdb.set_trace()
                        cropped_img.save("captcha.png")# salvando a imagem
                        sleep(2)
                        # passando o caminho de instalação do tesseract
                        ocr.pytesseract.tesseract_cmd = r'C:\Users\cgt\AppData\Local\Tesseract-OCR\tesseract.exe'
                        # convertendo a imagem capturada em texto
                        texto = ocr.image_to_string(Image.open('captcha.png'), lang='por')
                        texto = int(texto)
                        print(texto)
                        # buscando o input para inserir o texto
                        box_to_insert_code = browser.find_element_by_id("formularioPesquisa:validacaoImagem")
                        # inserindo o texto no input
                        box_to_insert_code.send_keys(texto)
                        # enviando o form
                        box_to_insert_code.submit()

                        # -- captura dos dados - Pagamentos por Nível de Bolsa --
                        #ul =  browser.find_element_by_xpath('//*[@id="tabContainerEntidadeEnsinoNivel"]/ul')
                        ul =  browser.find_element_by_css_selector("nav nav-tabs")
                        #tabs = ul.find_elements_by_xpath(".//li")
                        tabs = ul.find_elements_by_css_selector("li")
                        qtd_tabs = len(tabs)
                        print(qtd_tabs)
                        x = 0
                        import pdb; pdb.set_trace()
                        for row in tabs:
                            #print([a.text for a in row.find_elements_by_xpath('//*[@id="tabContainerEntidadeEnsinoNivel"]/ul/li['+ str(x) +']/a'])
                            # nome da moeda - BRL ou FRF ou DEM ou GBP etc.moeda = row.find_element_by_css_selector("li").text
                            moeda = row.find_element_by_css_selector("li").text
                            print([a.text for a in row.find_element_by_css_selector("li")])
                            tab = row.find_element_by_css_selector("a.link")
                            url_tab = tab.get_attribute("href")
                            url_tab.click()
                            conteudo = browser.find_element_by_class_name("tab-content")
                            div_conteudo = conteudo.find_element_by_id("tabItemEntidadeEnsinoNivel-"+x)
                            grid = div_conteudo.find_element_by_class_name("table-responsive height-limit")
                            linhas = grid.find_elements_by_tag_name("tr")
                            dados = linhas.find_elements_by_tag_name("td")
                            nivel = dados.find_element_by_tag_name('a').text
                            valor = dados.find_element_by_tag_name('span').text
                            table_total = conteudo.find_element_by_class_name('table')


                            if qtd_tabs > 1:
                                x = 1
                                tabs.click()
                                # se tiver mais de uma tab
                                dados = row.find_element_by_id("tabItemEntidadeEnsinoNivel-"+x)




                        # ------------- fim captura ----------------------------
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

exit()
# -------------------------- codigo de teste para tirar um print da pagina ----
browser.save_screenshot("pg_main.tif")

# ----- lendo a imagem e recortando o captcha -----
img = Image.open(r"pg_main.tif")# abrindo a screenshot salva
# import pdb; pdb.set_trace()
border = (366, 585, 615, 660) # left, up, right, bottom - selecionando a imagem
cropped_img = img.crop(border)# cortando apenas o tamanho do captcha
# import pdb; pdb.set_trace()
cropped_img.save("captcha.png")# salvando a imagem
sleep(2)
# tem que passar o caminho de instalação do tesseract
ocr.pytesseract.tesseract_cmd = r'C:\Users\cgt\AppData\Local\Tesseract-OCR\tesseract.exe'
texto = ocr.image_to_string(Image.open('captcha.png'), lang='por')
print(texto)
#import pdb; pdb.set_trace()
#print("FIM")
#browser.quit()
# -----------------------------------------------------------------------------
























# --------------------------------- fim do codigo teste ----------------------------------------------
