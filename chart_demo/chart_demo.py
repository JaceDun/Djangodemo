# -*- coding: utf-8 -*-
import time, json, random
from flask import Flask, render_template, request
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1> hello flask !</h1>'


@app.route("/get_json")
def get_json():
    return '{"status":"ok"}'


@app.route("/wsocket")
def websocket_connect():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']

        if not ws:
            return '{"status": "error", "message": "request is not websocket"}'
        else:
            # while(1):
            print("client connected")
            data1 = [[600, 300], [800, 300], [800, 400], [600, 400]]
            postdata = [{"offsetX": 0, "offsetY": 0}, {"offsetX": 0, "offsetY": 0}]
            for i in range(50):
                # try:
                #    message = ws.receive()
                # except WebSocketError:
                #    break
                # print(message)

                data = [data_generate(30), data_generate(30)]

                postdata[0]["offsetX"] = data1[i % 4][0] +  random.randint(0, 15)
                postdata[0]["offsetY"] = data1[i % 4][1] +  random.randint(0, 15)

                response = {"status": "ok", "message": postdata}
                response = json.dumps(response)
                ws.send(response)
                time.sleep(3)


    else:
        return '{"status": "error", "message": "request is not websocket"}'


def data_generate(x):
    location = {"offsetX": 0, "offsetY": 0}
    location["offsetX"] = random.randint(0, x)
    location["offsetY"] = random.randint(0, x)
    return location


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080, debug=True)
    http_server = WSGIServer(('0.0.0.0', 8080), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
