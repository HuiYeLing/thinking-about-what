from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('my_get', methods=['GET'])
def my_get():
    username = request.args.get('username')
    password = request.args.get('password')
    return f"接收到的参数，分别为:username:{username},password:{password}" #http请求对应的内容

if __name__=='__main__' :
    app.run()