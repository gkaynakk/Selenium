from selenium import webdriver
from selenium.webdriver.common.keys import Keys # we are going to be able to type something  in the search bar and see it in the results
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

### Web Scraping, Bots & Testing

PATH =("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH) # We installed chromewebdriver and assigned it to a variable with given PATH

driver.get("https://website.com") # Opens the webpage
print(driver.title) # Gets the title

### Locating Elements From HTML

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"main"))
    ) # Basically telling driver to wait 10 secs until indicated ID is located 
    # print(main.text) 
    
    articles  = main.find_elements_by_tag_name("article") # we looked for specific tag inside of main
    for article in articles: # we looped through all the articles
        header = article.find_element_by_class_name("entry-summary") # We are going to look for class name "entry-summary" in tag name "article"
        print(header.text) 
finally:
    driver.quit()

# print(driver.page_source) - way to access source code

# time.sleep(5) - Results stays for 5 secs before quit


print(main.text)

driver.quit() # Instantly quits
