from flask import Flask, request
import json

app = Flask(__name__)


# Endpoint to receive webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Write JSON data to a file
        with open('webhook_data.txt', 'w') as file:
            json.dump(json_data, file)

        return 'Webhook data received successfully', 200
    except Exception as e:
        return str(e), 500


# app.run()
app.run(host='0.0.0.0', port=80, debug=True)

