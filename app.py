from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return {'message': 'Hello, World!'}



@app.route('/hello_world/<name>')
def hello_world_name(name):
    return {'message': 'Hello, ' + name + ' World!'}


@app.route('/hello_world/long')
def hello_world_long():
    # mock a long running task
    time.sleep(60)
    # return a response
    return {'message': 'Hello, World!'}

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    return {'message': f'Hello, {name}! This is a POST response.'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
