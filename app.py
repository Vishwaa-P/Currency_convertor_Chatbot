from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    
    # Extract parameters from Dialogflow
    # Make sure these names match your Dialogflow Parameter names exactly!
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    # Get the conversion factor
    cf = fetch_conversion_factor(source_currency, target_currency)
    
    if cf is None:
        # Fallback if the API fails
        return jsonify({'fulfillmentText': "Sorry, I couldn't get the exchange rate right now."})

    final_amount = amount * cf
    final_amount = round(final_amount, 2)
    
    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    }
    return jsonify(response)

def fetch_conversion_factor(source, target):
    # Using Frankfurter API (No API Key required)
    url = "https://api.frankfurter.app/latest?from={}&to={}".format(source, target)
    
    try:
        response = requests.get(url)
        data = response.json()
        # The API returns data like: {"rates": {"INR": 83.20}}
        return data['rates'][target]
    except:
        return None

if __name__ == "__main__":
    # Running on Port 5001 to avoid Mac AirPlay conflict
    app.run(port=5001, debug=True)