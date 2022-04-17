from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd

url = "https://www.propertyguru.com.sg/singapore-property-listing/hdb/jurong-west/boon-lay-place_103145/211/last-transacted-prices-and-insights"
driver = webdriver.Chrome(service=Service("./chromedriver"))
driver.get(url)

month = []
resale_price = []

for i in range(1, 25 + 1):
    xpath_date = f"/html/body/div[2]/div/div/section[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/ul[1]/li[{i}]/div[1]/p"
    xpath_price = f"/html/body/div[2]/div/div/section[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/ul[1]/li[{i}]/div[3]/p[1]"

    date_raw = driver.find_element(value=xpath_date, by=By.XPATH).text
    price_raw = driver.find_element(value=xpath_price, by=By.XPATH).text

    date = str(datetime.strptime(date_raw, '%b %Y'))[:10]
    price = price_raw.split()[1].replace(",", "")

    month.append(date)
    resale_price.append(price)

    print(date, price)

test_data = pd.DataFrame({"month": month, "resale_price": resale_price})
test_data.to_csv("./data_arima/test_data.csv", index=False)
driver.quit()
