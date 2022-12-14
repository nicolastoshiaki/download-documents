import pandas as pd 
import pyperclip as pc 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 

df = pd.read_excel(r'excel_file_path')
navegador = webdriver.Chrome() 
navegador.get("front_url") 

if navegador.find_element(By.XPATH,'//[@id=\"details-button\"]'):
    navegador.find_element(By.XPATH,'//[@id=\"details-button\"]').send_keys(Keys.ENTER)
    navegador.find_element(By.XPATH,'//[@id=\"proceed-link\"]').send_keys(Keys.ENTER) 
    
for index, row in df.iterrows(): 
    proposta = str(row['PROPOSTA']) 
    pc.copy(proposta) 
    navegador.find_element(By.XPATH,'xpath_id').click() 
    navegador.find_element(By.XPATH,'xpath_id').click() 
    navegador.find_element(By.XPATH,'xpath_id').send_keys(Keys.CONTROL+"v") 
    navegador.find_element(By.XPATH,'xpath_id').click(), 
    navegador.find_element(By.XPATH,'xpath_id').click()