### Page Navigating and Clicking Elements

PATH =("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(PATH) # We installed chromewebdriver and assigned it to a variable with given PATH

driver.get("https://website.com") # Opens the webpage

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Python Project"))
    ) # Basically telling driver to wait 10 secs until indicated LINK_TEXT is located 
    element.click()
    
    element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    ) # Basically telling driver to wait 10 secs until indicated ID is located 
    element.click()
    
    driver.back()
    driver.back()
    driver.back() # Just goes back!
    driver.forward()
    driver.forward() # Goes forward!
except:
    driver.quit()
