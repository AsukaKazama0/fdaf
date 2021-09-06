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

def coingecko(token):
	url = "https://coincodex.com/api/coincodex/get_coin/" + str(token)
	response = requests.get(url)
	return response.json()


	
	
