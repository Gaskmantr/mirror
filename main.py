import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://mirror-h.org/site-send'
browser.get(url)
nick = input("İsim:")
time.sleep(5)
print("20")
with open("site.txt", "r") as f:
    for line in f:
        line.strip("\n")
        username = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/form/div[1]/input[1]")
        username.send_keys(nick)

        zone = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/form/div[2]/input")
        zone.send_keys(line)

        click = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/form/button")
        click.click()