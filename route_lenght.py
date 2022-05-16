from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
def get_route_lenght(start, finish):
    driver = webdriver.Chrome(options=options,executable_path=r"C:\Program Files\Chromedriver\chromedriver.exe")
    driver.get("https://www.google.com/maps")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'hArJGc').click()
    driver.find_element(By.XPATH,"//*[@id='sb_ifc51']/input").send_keys(start)
    driver.find_element(By.XPATH,"//*[@id='sb_ifc52']/input").send_keys(finish)
    driver.find_element(By.XPATH,"//*[@id='directions-searchbox-1']/button[1]").click()
    len_ele = driver.find_element(By.XPATH, "//div[contains(text(),'km')]")
    lenght=len_ele.text[:-3]
    if '.' in lenght[1]:
        lenght = float(lenght) * 1000
    if ',' in lenght:
        lenght=lenght.replace(",", ".")
    return float(lenght)


