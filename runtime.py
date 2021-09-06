
import os
import urllib.request
import base64
import requests
import random


def coingecko(token):
	url = "https://coincodex.com/api/coincodex/get_coin/" + str(token)
	response = requests.get(url)
	return response.json()


	
	
