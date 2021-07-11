from selenium import webdriver
from PIL import Image,ImageDraw, ImageFont
from io import BytesIO
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

import random

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'



def getUri(cop,cop2,timeFrame,theme,source):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	symbol = cop;
	driver.get('https://in.tradingview.com/chart/?symbol={}%3{}{}&interval={}&theme={}'.format(source,symbol,cop2,timeFrame,theme))
	wait = WebDriverWait(driver, 20)


	elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.chart-gui-wrapper')))
	clickable = driver.find_element_by_id('header-toolbar-screenshot').click();
	time.sleep(9)
	y = driver.find_element_by_class_name('input-3bEGcMc9').get_attribute("value")

	driver.quit()
	return y
