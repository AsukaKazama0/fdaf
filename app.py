from flask import Flask
from flask import request
from runtime import *
app = Flask(__name__)
app.debug = False
app.SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/api/v4/coc", methods=["GET"])
def coc():
        s =  request.args.get("s")
        returnUri = coingecko(s)
        return returnUri

