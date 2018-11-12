from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument("incognito")

browser = webdriver.Chrome(executable_path='C:/Users/Admin/Downloads/chromedriver', chrome_options=option)

browser.get("https://github.com/TheDancerCodes")

# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@id='js-pjax-container']/div/div[1]/a/img")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

    # find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class=’text-bold’]")
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')


#//*[@id="js-pjax-container"]/div/div[1]/a/img
