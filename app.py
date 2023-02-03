from flask import Flask, render_template, jsonify
from flask_cors import CORS
from handles.getData import *
import settings


app = Flask(__name__)
app.config.from_object(settings)
CORS(app)

# 数据接口
@app.route('/')

def index():
    return render_template('datas.html')

@app.route('/task1', methods=['GET'])
def task1():
    data = h_task1()
# jsonify的作用是将传入的json形式数据序列化成为json字符串
    return jsonify(data)

@app.route('/task2', methods=['GET'])
def task2():
    data = h_task2()
    return jsonify(data)

@app.route('/task3', methods=['GET'])
def task3():
    data = h_task3()
    return jsonify(data)

@app.route('/task4', methods=['GET'])
def task4():
    data = h_task4()
    return jsonify(data)

@app.route('/task5', methods=['GET'])
def task5():
    data = h_task5()
    return jsonify(data)

@app.route('/task6', methods=['GET'])
def task6():
    data = h_task6()
    return jsonify(data)
@app.route('/task7', methods=['GET'])
def task7():
    data = h_task7()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)