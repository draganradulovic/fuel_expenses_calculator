from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
def get_fuel_price(country,fuel):
    driver = webdriver.Chrome(options=options,executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
    driver.get("https://autotraveler.ru/en/spravka/fuel-price-in-europe.html")
    driver.implicitly_wait(10)
    fuel=fuel.lower()
    country=country.capitalize()
    if 'Bosnia' in country:
        country='Bosnia'
    if fuel=='petrol':
        price_td=driver.find_element(By.XPATH,"//table[@id='benzin_euro']//a[contains(text(),'"+country+"')]/parent::td/following-sibling::td[1]")
        price=price_td.text[2:6]
        return float(price)
    elif fuel == 'diesel':
        price_td = driver.find_element(By.XPATH, "//table[@id='benzin_euro']//a[contains(text(),'" + country + "')]/parent::td/following-sibling::td[3]")
        price = price_td.text[2:6]
        return float(price)



