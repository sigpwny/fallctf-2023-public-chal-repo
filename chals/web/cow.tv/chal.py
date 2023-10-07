from flask import Flask, jsonify, request
import os

app = Flask(__name__, static_url_path='', static_folder='build')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/say', methods=['POST', 'GET'])
def cowsay():
    input = request.json.get('input', 'MOOOOOO')
    
    command = f'/usr/games/cowsay "{input}"'
    output = os.popen(command).read()

    return jsonify({
        'output': output
    })

if __name__ == '__main__':
    app.run(threaded=True, port=1337, host="0.0.0.0")