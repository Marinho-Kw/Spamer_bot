from bs4 import BeautifulSoup
import requests
import pyautogui
import time

def bot_spam(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    h = parse.find_all(tag)
    print(h)
    for mensagem in h:
        pyautogui.typewrite(mensagem.get_text())
        
        pyautogui.press('enter')
bot_spam('https://www.mensagens10.com.br/mensagens-de-bom-dia', 'p')

