from selenium import webdriver #For Selenium Web Driver
import os #For executing terminal commands as well as accessing directory
import requests #For Session
from time import sleep

url_main = "http://transparencia.capes.gov.br/transparencia/xhtml/index.faces" #Target Url
# url_sec = "http://transparencia.capes.gov.br/transparencia/xhtml/PesquisaEntidadeEnsino.faces"
# captcha_image_url = "http://transparencia.capes.gov.br/transparencia/img/captcha/captcha.jpg?v=" + '*' #This url is known by doing inspect element on captcha_image generated

#Store Credentials
username = "caca"
Password = "1234"

browser = webdriver.Chrome() #Loading Browser Instance
#browser = webdriver.Chrome(executable_path=os.curdir + '/chrome_driver_78') #Loading Browser Instance
#Note the binary_file_name is important in above line
#os.curdir gives the current directory location in which your code file is situated
browser.get(url_main) #Opening Target Url
link = browser.find_element_by_xpath('//*[@id="main"]/div[4]/div/div/div[2]/div[2]/div/div/a')
link.click()
sleep(3)

import pdb; pdb.set_trace()
# Creating Session so that same captcha image is loaded on opening the captcha_url as well as target_url
cookies = browser.get_cookies()
session = requests.Session()
#for cookie in cookies:
    #session.cookies.set(cookie['name'], cookie['value'])

# Downloading Image Captcha("captcha.jpeg" name is given to file)
import pdb; pdb.set_trace()
try:
    read = session.get(url_sec)
    with open("captcha.jpeg", 'wb') as w:
        for chunk in read.iter_content(chunk_size=512):
            if chunk:
                w.write(chunk)
except:
    print("Error Downloading Captcha")
    browser.quit()

os.system("cp captcha.jpeg " + os.curdir + "/ocr-convert-image-to-text")
print("File Copied")

# Using OCR-Tool to convert image to text
os.chdir(os.curdir + "/ocr-convert-image-to-text")
os.system("python3 main.py --input_dir captcha.jpeg --output_dir .")
print("captcha.txt generated")

# Reading captcha from file
with open("captcha.txt", "r") as captcha_file:
    for line in captcha_file:
        captcha_text = line.strip()
        break

print("Captcha = " + captcha_text)


#All the elements refer to html elements in html code and the name(unique identifier) of each tag used in html code
#Selecting Form Fields
username_element = browser.find_element_by_name('txt_username')
password_element = browser.find_element_by_name('txt_password')
captcha_element = browser.find_element_by_name('txtcaptcha')
submit_btn = browser.find_element_by_id('btnSubmit')

# Filling up Form by credentials gathered
username_element.send_keys(username)
password_element.send_keys(password)
captcha_element.send_keys(captcha_text)

# Submitting Form
submit_btn.click()
