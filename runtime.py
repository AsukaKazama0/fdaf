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
import urllib.request
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
	pos = (0,50)

	elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.chart-gui-wrapper')))
	clickable = driver.find_element_by_id('header-toolbar-screenshot').click();
	time.sleep(4)
	lem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.copyForm-1aOR8tBW')))
	y = driver.find_element_by_class_name('input-3bEGcMc9').get_attribute("value")
	url = y
	r = requests.get(url, allow_redirects=True)
	filename = random.randint(10000000000000,99999999999999) + random.randint(10000000000000,99999999999999) 
	filename = "u" + str(filename) + ".png"
	urllib.request.urlretrieve(y,filename)
	opacity = 100 / 100
	OriImg = cv2.imread(filename, -1)
	waterImg = cv2.imread('./Logo.png', -1)
	tempImg = OriImg.copy()
	print(tempImg.shape)
	overlay = transparentOverlay(tempImg, waterImg, pos)
	output = OriImg.copy()
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

	url = "https://www.coingecko.com/en/coins/trending"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	driver.set_window_size(1080, 768)
	name = random.randint(000000,999999) + random.randint(000000,999999) + random.randint(00000000,99999999)
	name = str(name) + ".png"
	driver.get(url)
	driver.execute_script("window.scrollTo(0, 390)") 
	jsscript = "document.querySelector('#cookie-notice').style.display='none';"
	driver.execute_script(jsscript)

	driver.save_screenshot(name)
	
	
	with open(str(name), "rb") as file:
		url = "https://api.imgbb.com/1/upload"
		payload = {
		"key": "a859f23787a42e9036ec053e38b3999c",
		"image": base64.b64encode(file.read()),
		}
	res = requests.post(url, payload)
	y = res.json()['data']['display_url']
	os.remove(str(name))
	driver.quit()
	return y
def analysis(interval,symbol,theme):
	url = "https://s.tradingview.com/embed-widget/technical-analysis/?locale=in&interval={}&symbol={}&colorTheme={}"
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	driver.set_window_size(500, 700)
	name = random.randint(000000,999999) + random.randint(000000,999999) + random.randint(00000000,99999999)
	name = str(name) + ".png"
	driver.get(url.format(interval,symbol,theme))
	dwait = WebDriverWait(driver, 20)
	dwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.speedometersContainer-DPgs-R4s')))
	getHtml = """element = document.querySelector(".speedometersContainer-DPgs-R4s");
	element.innerHTML += "<div class='ButterImg'><img class='ButterLemon' src='https://i.ibb.co/j4nhYg8/Logo-3.png'/></div>";
	elementp = document.querySelector('.ButterImg');
	elementp.style.display = 'flex';
	elementp.style.width = '100%';
	elementp.style.justifyContent = 'center' """
	driver.execute_script(getHtml) 
# 	jsscript = "document.querySelector('#cookie-notice').style.display='none';"
# 	driver.execute_script(jsscript)
	dwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ButterLemon')))

	driver.save_screenshot(name)
	
	
	with open(str(name), "rb") as file:
		url = "https://api.imgbb.com/1/upload"
		payload = {
		"key": "a859f23787a42e9036ec053e38b3999c",
		"image": base64.b64encode(file.read()),
		}
	res = requests.post(url, payload)
	y = res.json()['data']['display_url']
	os.remove(str(name))
	driver.quit()
	return y
def getStock(cop,timeFrame,theme):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	# chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	
	driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=chrome_options)
	driver.set_window_size(1920,1080)
	symbol = cop;
	driver.get('https://s.tradingview.com/mediumwidgetembed/?symbols={}&locale=in&&colorTheme={}'.format(symbol,theme.lower()))
	wait = WebDriverWait(driver, 20)
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".options-1TbOurr7")))
	if timeFrame is '1D':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(1)").click()
	elif timeFrame is '1M':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(2)").click()
	elif timeFrame is '3M':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(3)").click()
	elif timeFrame is '1Y':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(4)").click()
	elif timeFrame is '5Y':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(5)").click()
	elif timeFrame is 'ALL':
		elem = driver.find_element_by_css_selector(".options-1TbOurr7 .option-1TbOurr7:nth-child(6))").click()
	time.sleep(3)	
	filename = random.randint(10000000000000,99999999999999) + random.randint(10000000000000,99999999999999) 
	filename = "u" + str(filename) + ".png"
	getHtml = """
	var elem = document.createElement('div');
	elem.style.cssText = 'display:flex;position:absolute;width:100%;justify-content:center;z-index:99999;top:5px;';
	document.body.appendChild(elem);
	elem.innerHTML = "<div class='ButterImg'><img class='ButterLemon' src='https://i.ibb.co/j4nhYg8/Logo-3.png'/></div>"
"""
	driver.execute_script(getHtml) 
	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ButterLemon')))

	driver.save_screenshot(filename)

	with open(filename, "rb") as file:
		url = "https://api.imgbb.com/1/upload"
		payload = {
			"key": "a859f23787a42e9036ec053e38b3999c",
			"image": base64.b64encode(file.read()),
		}
		res = requests.post(url, payload)
	y = res.json()['data']['image']["url"]
	os.remove(filename)
	return y

	
	
