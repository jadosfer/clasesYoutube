from selenium import webdriver
import time

def mensajea():

    driver = webdriver.Chrome()
    driver.get('http://web.whatsapp.com')

    name = "Rocío Biroli"
    msg = 'si esto me sale bien vas a recibir este mensaje 5 veces cada 3 seg. y lo estoy mandando desde Python!! Me va a avisar cuando pase algo en la bolsa'

    #Scan the code before proceeding further
    input("Enter anything after scanning QR code: ")

    user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    
    for i in range(5):
        msg_box.send_keys(msg)
        driver.find_element_by_class_name('_1U1xa').click()
        time.sleep(3)

mensajea()

