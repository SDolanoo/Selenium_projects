from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.euro.com.pl/pojazdy-elektryczne/acer-hulajnoga-elektr-acer-es-series-3\
# .bhtml?gad_source=1&gclid=Cj0KCQjw2PSvBhDjARIsAKc2cgMTOH3aB-21Hr7RNCSU7xh1tATfUQDmTRO0zC0NlkCtV\
# uvu55W4-G8aAkEoEALw_wcB&gclsrc=aw.ds")
#
# price_pln = driver.find_element(By.CLASS_NAME, value='price-template__large--total')
# price_fraction = driver.find_element(By.CLASS_NAME, value='price-template__large--decimal')
# print(f"Cena to {price_pln.text}.{price_fraction.text}")

# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documantation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documantation_link.text)
bug_link = driver.find_element(By.XPATH, value='/html/body/ems-root/eui-root/eui-dropdown-host/div[2]/ems-euro-mobile\
/ems-product/ems-euro-mobile-product-page/div/ems-euro-mobile-product-card/div/div[1]/div/eui-tabs/div/button\
[1]/span/div/ems-price/div/div/div/span[2]')
print(bug_link.text)

# driver.close()
driver.quit()
