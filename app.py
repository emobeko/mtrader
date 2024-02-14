from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    return 'Trade signal received', 200


@app.route('/get_signal', methods=['GET'])
def get_signal():
    return jsonify({"action": "BUY", "symbol": "EURUSD", "quantity": 0.1})


# app.run()
app.run(host='0.0.0.0', port=80, debug=True)

