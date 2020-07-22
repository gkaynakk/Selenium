### ActionChains & Automating Cookie Clicker!

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH =("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH) # We installed chromewebdriver and assigned it to a variable with given PATH

driver.get("https://orteil.dashnet.org/cookieclicker/") # Opens the webpage

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for  i in range(1,-1,-1)]

actions = ActionChains(driver) # We creted a new ActionsChains object that's going to act on the driver and we stored it in a variable
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
    
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
