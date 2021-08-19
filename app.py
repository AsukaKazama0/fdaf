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
        json = {"code": 200,"result":"sucess","imgUri":returnUri }
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
def analy():
    symbol = request.args.get('s')
    interval = request.args.get('time')
    theme = request.args.get('theme')
    theme = str(theme).lower()
    if theme == None:
        theme == "dark"
    if interval == None:
        interval = '15m'
    if symbol != None:
        returnUri = analysis(interval,symbol,theme)
        json = {"code": 200,"result":"sucess","imgUri":returnUri }
    else:
        json = """{"code": 500,
        "result":"error"
        }"""
    return json
@app.route("/api/v4/stock", methods=["GET"])
def routage:
    symbol = request.args.get('s')
    theme = request.args.get('theme')
    interval = request.args.get('time')
    
    theme = str(theme).lower()
    if interval == None:
        interval = '1D'
    if theme == None:
        theme == "dark"
    if symbol != None:
        
        returnUri = getStock(symbol,interval,theme)
        json = {"code": 200,"result":"sucess","imgUri":returnUri }
