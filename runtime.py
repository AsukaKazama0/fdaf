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
import base64
import requests
import random
import cv2
from PIL import *
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# CHROMEDRIVER_PATH = './chromedriver'

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][0] / 255.0)  # read the alpha channel
            src[x + i][y + j] += overlay[i][j][:3]
    return src


def getUri(cop,cop2,timeFrame,theme,source):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	driver.set_window_size(1920,1080)
	symbol = cop;
	driver.get('https://www.tradingview.com/widgetembed/?frameElementId=tradingview_9aa27&symbol={}&interval={}&theme={}&exchange={}'.format(symbol,timeFrame,theme,source))
	wait = WebDriverWait(driver, 20)


	elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.chart-gui-wrapper')))
	clickable = driver.find_element_by_id('header-toolbar-screenshot').click();
	time.sleep(4)
	lem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.copyForm-1aOR8tBW')))
	y = driver.find_element_by_class_name('input-3bEGcMc9').get_attribute("value")
	url = y
	r = requests.get(url, allow_redirects=True)
	filename = random.randint(10000000000000,99999999999999) + random.randint(10000000000000,99999999999999) 
	filename = "u" + str(filename) + ".png"
    	opacity = opacity / 100
    	OriImg = cv2.imread(MainImage, -1)
    	waterImg = cv2.imread(LogoImage, -1)
    	tempImg = OriImg.copy()
    	print(tempImg.shape)
    	overlay = transparentOverlay(tempImg, waterImg, pos)
    	output = OriImg.copy()
    	# apply the overlay
    	cv2.addWeighted(overlay, opacity ,output, 1 - opacity, 0, output)
    	filename = random.randint(10000000000000,99999999999999) + random.randint(10000000000000,99999999999999) 
   	 filename = "u" + str(filename) + ".png"
    	cv2.imwrite(filename,output)
    	with open(filename, "rb") as file:
    		url = "https://api.imgbb.com/1/upload"
    		payload = {
        		"key": "a859f23787a42e9036ec053e38b3999c",
        		"image": base64.b64encode(file.read()),
    		}
    		res = requests.post(url, payload)
    	y = res.json()['data']['url_viewer']


	return y
def coingecko():
	url = "https://www.coingecko.com/en/coins/trending"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	name = random.randint(000000,999999)
	name = name , ".png"
	driver.get(url)
	elem = driver.find_element_by_css_selector(".container ").screenshot(str(name))
	
	with open(str(name), "rb") as file:
		url = "https://api.imgbb.com/1/upload"
		payload = {
		"key": "a859f23787a42e9036ec053e38b3999c",
		"image": base64.b64encode(file.read()),
		}
		res = requests.post(url, payload)
	return y
	
	
