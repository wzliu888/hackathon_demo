from flask import Flask, request, Response
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
    return {'message': 'Hello, World! Long running task done.'}

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    print(data) # log can be seen in the terminal
    name = data.get('name', 'Anonymous')
    return {'message': f'Hello, {name}! This is a POST response.'}

@app.route('/sse')
def sse():
    def event_stream():
        count = 0
        while True:

            if count == 10:
                break

            count += 1
            # Send a message every second
            yield f"data: {{\"count\": {count}, \"time\": \"{time.strftime('%H:%M:%S')}\"}}\n\n"
            time.sleep(1)
    
    return Response(event_stream(), mimetype='text/event-stream', headers={
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'X-Accel-Buffering': 'no'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
