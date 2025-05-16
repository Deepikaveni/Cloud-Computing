from flask import Flask, request, jsonify
from flask_cors import CORS
from plaid import Client
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for local frontend testing

# --- Plaid Client Configuration ---
client = Client(
    client_id='PLAID_CLIENT_ID',
    secret='PLAID_SECRET',
    environment='sandbox'  # or 'development' or 'production'
)

# --- Step 1: Exchange Public Token ---
@app.route('/api/exchange_token', methods=['POST'])
def exchange_token():
    public_token = request.json.get('public_token')
    try:
        exchange_response = client.Item.public_token.exchange(public_token)
        access_token = exchange_response['access_token']
        return jsonify({'access_token': access_token})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Step 2: Fetch Transactions ---
@app.route('/api/transactions', methods=['POST'])
def fetch_transactions():
    access_token = request.json.get('access_token')
    try:
        response = client.Transactions.get(access_token, start_date='2023-01-01', end_date='2023-12-31')
        transactions = response['transactions']
        return jsonify(transactions)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
Fetch data
// Send public_token to backend
fetch('http://localhost:5000/api/exchange_token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ public_token })
})
.then(res => res.json())
.then(data => {
  const access_token = data.access_token;

  // Then fetch transactions
  return fetch('http://localhost:5000/api/transactions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ access_token })
  });
})
.then(res => res.json())
.then(transactions => {
  console.log(transactions);  // You can feed this to your chart/table
});

