from flask import Flask, request, jsonify
import requests
import os  # <--- IMPORT THIS

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    cf = fetch_conversion_factor(source_currency, target_currency)
    
    if cf is None:
        return jsonify({'fulfillmentText': "Sorry, I couldn't get the exchange rate right now."})

    final_amount = amount * cf
    final_amount = round(final_amount, 2)
    
    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)

def fetch_conversion_factor(source, target):
    url = "https://api.frankfurter.app/latest?from={}&to={}".format(source, target)
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates'][target]
    except:
        return None

if __name__ == "__main__":
    # Get the PORT from the environment variables (Render sets this automatically)
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
