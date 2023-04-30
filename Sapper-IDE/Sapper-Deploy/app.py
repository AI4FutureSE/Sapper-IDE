from flask import Flask, request, render_template
from flask_cors import CORS
import json
from UserProject.Chatbot.GenCode import Chatbot
from UserProject.Todos.GenCode import Todos
from UserProject.wenxiaojie.GenCode import wenxiaojie
from UserProject.qingxiaoxie.GenCode import qingxiaoxie
from UserProject.yunxiaojuan.GenCode import yunxiaojuan
from UserProject.sixiaopin.GenCode import sixiaopin
from UserProject.maxiaoyuan.GenCode import maxiaoyuan
from UserProject.chunxiaoxie.GenCode import chunxiaoxie
from UserProject.xinxiaozhu.GenCode import xinxiaozhu
from UserProject.huixiaoshi.GenCode import huixiaoshi
from UserProject.AirSim.GenCode import AirSim
# import gevent.pywsgi
# import gevent.monkey
# from flask_sslify import SSLify

app = Flask(__name__)
CORS(app)
# sslify = SSLify(app)
# CORS(app, supports_credentials=True)

@app.route('/service/<service>',methods = ['POST','GET'])
def service(service):
    return render_template("service.html", service = f"{service}")

@app.route('/<service>',methods = ['POST','GET'])
def service1(service):
    return render_template("service.html", service = f"{service}")

@app.route('/AirSimUrl',methods = ['POST','GET'])
def Sapper_AirSim():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = AirSim(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/ChatbotUrl',methods = ['POST','GET'])
def Sapper_Chatbot():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = Chatbot(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/TodosUrl',methods = ['POST','GET'])
def Sapper_Todos():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = Todos(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/wenxiaojieUrl',methods = ['POST','GET'])
def Sapper_wenxiaojie():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = wenxiaojie(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/qingxiaoxieUrl',methods = ['POST','GET'])
def Sapper_qingxaioxie():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = qingxiaoxie(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/yunxiaojuanUrl',methods = ['POST','GET'])
def Sapper_yunxiaojuan():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = yunxiaojuan(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/sixiaopinUrl',methods = ['POST','GET'])
def Sapper_sixiaopin():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = sixiaopin(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/maxiaoyuanUrl',methods = ['POST','GET'])
def Sapper_maxiaoyuan():
    if request.method == 'POST':
        print(request)
        query = request.json
        print(query)
        answer = maxiaoyuan(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/chunxiaoxieUrl',methods = ['POST','GET'])
def Sapper_chunxiaoxie():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = chunxiaoxie(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/xinxiaozhuUrl',methods = ['POST','GET'])
def Sapper_xinxioazhu():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = xinxiaozhu(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

@app.route('/huixiaoshiUrl',methods = ['POST','GET'])
def Sapper_huixiaoshi():
    if request.method == 'POST':
        query = request.form
        print(query)
        answer = huixiaoshi(query)
        print(json.dumps(answer))
        # answer是json文件
        return json.dumps(answer)

if __name__ == '__main__':
    # app.run(processes=True,debug=False,port=5000,ssl_context=('fullchain.pem', 'privkey.key'),host='0.0.0.0')
    # gevent_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5000),app)
    # gevent_server.serve_forever()
    app.run(debug=False, port=5001)
