from flask import Flask
from flask import request
from runtime import *
app = Flask(__name__)
app.debug = False
app.SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/api/v4/", methods=["GET"])
def cop():
    s =  request.args.get("s")
    s2 = request.args.get('sn')
    timeFrame =request.args.get('timeFrame')
    theme = request.args.get('theme')
    source = request.args.get('source')
    if theme == None:
        theme = 'dark'
        
    if source == None:
        source = 'BINANCE'
    if timeFrame == None:
        timeFrame = '4H'
    if s != None:
        if s2 == None:
           s2 = 'USDT'
        returnUri = getUri(s,s2,timeFrame,theme,source)
        json = {"cod": 200,"result":"sucess","imgUri":returnUri }
    else:
        json = """{"code": 500,
        "result":"error"
        }"""
    return json
@app.route("/api/v4/coc", methods=["GET"])
def coc():
        returnUri = coingecko()
        return returnUri
@app.route("/api/v4/analysis", methods=["GET"])
def coc():
    symbol = request.args.get('s')
    interval = request.args.get('time')
    returnUri = alaysis(interval,symbol)
    return returnUri
