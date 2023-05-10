from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/even-odd', methods=['POST'])

def even_odd():
    num = request.form['num']
    if int(num) % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    return jsonify(result=result)

@app.route('/prime', methods=['POST'])

def prime():
    num = int(request.form['num'])
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                result = 'Not Prime'
                break
        else:
            result = 'Prime'
    else:
        result = 'Not Prime'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
