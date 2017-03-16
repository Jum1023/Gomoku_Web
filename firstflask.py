#coding=UTF-8
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("gobang.html")

if __name__ == '__main__':
    # app.run() #只有本机可以访问，外部主机无法访问
    app.run(host='0.0.0.0')  #使你的服务器公开可用