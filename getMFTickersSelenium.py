from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://finance.yahoo.com/screener')

#driver.maximize_window()

driver.implicitly_wait(30)

MFscreener = driver.find_element(by=By.CSS_SELECTOR, value='a[title="Mutual Fund Screener"]')
MFscreener.click()

# deselect all options
driver.find_element(by=By.CSS_SELECTOR, value="[title='Remove Exchange']").click()
driver.find_element(by=By.CSS_SELECTOR, value="[title='Remove Funds by Category']").click()
driver.find_element(by=By.CSS_SELECTOR, value="[title='Remove Funds by Company']").click()
driver.find_element(by=By.CSS_SELECTOR, value="[title='Remove Morningstar Performance Rating Overall']").click()
driver.find_element(by=By.CSS_SELECTOR, value="[title='Remove Price (Intraday)']").click()

driver.find_element(by=By.CSS_SELECTOR, value='button.addFilter').click()
driver.find_element(by=By.XPATH , value='//span[text()="Region"]/../../input').click()
driver.find_element(by=By.XPATH , value='//span[text()="Morningstar Performance Rating Overall"]/../../input').click()
driver.find_element(by=By.XPATH , value='//span[text()="Close"]/..').click()

time.sleep(6)

failed = True
while failed:
    try:
        driver.find_element(by=By.CSS_SELECTOR , value='li.filterAdd').click()
        failed = False
    except:
        print('filterAdd failed, try again')
        time.sleep(1)

driver.find_element(by=By.XPATH , value='//span[text()="United States"]/../input').click()
driver.find_element(by=By.CSS_SELECTOR , value='button[aria-label="Close"]').click()

driver.find_element(by=By.CSS_SELECTOR , value='button[title="★★★"]').click()

# wait a bit till all commercial crap updates
time.sleep(3)

#<span>Mutual Funds</span>
findStock = driver.find_element(by=By.CSS_SELECTOR , value='button[data-test="find-stock"]')
findStock.click()

time.sleep(10)

quotes = driver.find_elements(by=By.CSS_SELECTOR , value='a[data-test="quoteLink"]')
quotes[-10].location_once_scrolled_into_view

print('moved to bottom')
#<span>Show 25 rows</span>
driver.find_element(by=By.XPATH , value='//span[text()="Show 25 rows"]').click()

print('clicked 0n Show 25 rows')
#print('wait 10')
#time.sleep(10)

driver.find_element(by=By.XPATH , value='//span[text()="Show 100 rows"]').click()

print('clicked 0n Show 100 rows')
print('wait 4')
time.sleep(4)

quotes = driver.find_elements(by=By.CSS_SELECTOR , value='a[data-test="quoteLink"]')
quotes[-10].location_once_scrolled_into_view

print('moved to bottom')

foundQuotes = []
page = 1;
while(True):
    print('%s: page %s: %s quotes' % (time.asctime(), page, len(quotes)))
    for quote in quotes:
        qtext = ''
        try:
            qtext = quote.text
            foundQuotes.append(qtext)
        except:
            print('could not get quote text')

    if len(quotes) != 100: break
    nextButton = driver.find_element(by=By.XPATH , value='//span[contains(text(), "Next")]')
    #nextButton.location_once_scrolled_into_view
    nextButton.click()
    page = page + 1
    time.sleep(4)
    failed = True
    while failed:
        try:
            quotes = driver.find_elements(by=By.CSS_SELECTOR , value='a[data-test="quoteLink"]')
            failed = False
        except:
            print('list not found, try again')
            time.sleep(1)
    if len(quotes) == 0: break
    max(0, len(quotes) -10)
    quotes[max(0, len(quotes) -10)].location_once_scrolled_into_view

print('Found total of %s quotes' % len(foundQuotes))
#time.sleep(10)