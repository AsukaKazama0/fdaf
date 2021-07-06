from flask import Flask
from flask import request
from runtime import getUri
app = Flask(__name__)
app.debug = True


@app.route("/api/v4/", methods=["GET"])
def cop():
    s =  request.args.get("s")
    s2 = request.args.get('sn')

    if s != None:
        if s2 == None:
            s2 = 'USDT'
        returnUri = getUri(s,s2)
        json = {"code": 200,"result":"sucess","imgUri":returnUri }
    else:
        json = """{"code": 500,
        "result":"error"
        }"""
    return json

app.run()