driver = webdriver.Chrome('/Users/shelar/Downloads/chromedriver')

driver.get("https://web.whatsapp.com/")

sleep(20)

# input("Plese scan qr code and press: ")

RM = driver.find_element_by_xpath('//span[@title = "Bhushan"]')

RM.click()

testinput = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            testinput.send_keys("hello bhushan this is the automation test message ")

sleep(2)

testinput.send_keys(Keys.RETURN)
            
print("\t\t\t\n********************** Whatsapp Successfully Sended *********************************\n")
