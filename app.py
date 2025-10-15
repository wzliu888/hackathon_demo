from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
