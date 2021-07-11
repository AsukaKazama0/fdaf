from flask import Flask
from flask import request
from runtime import getUri
app = Flask(__name__)
app.debug = False
app.SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/api/v4/", methods=["GET"])
def cop():
    s =  request.args.get("s")
    s2 = request.args.get('sn')
    timeFrame =reqquest.args.get('timeFrame')
    Theme = request.args.get('Theme')
    source = request.args.get('source')
    if Theme == None:
        theme = 'DARK'
    if source == None:
        source = 'Binance'
    if timeFrame == None:
        timeFrame = '4H'
    if s != None:
        if s2 == None:
           s2 = 'USDT'
        returnUri = getUri(s,s2,timeFrame,Theme,source)
        json = {"cod": 200,"result":"sucess","imgUri":returnUri }
    else:
        json = """{"code": 500,
        "result":"error"
        }"""
    return json
