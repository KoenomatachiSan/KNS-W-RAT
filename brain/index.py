from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/order', methods=['GET'])
def order():
    return {
        "keep_alive":True
    }

@app.route('/transaction_result', methods=['POST'])
def transaction_result():
    result = request.get_json()
    print(result)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)