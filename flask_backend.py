from flask import request
from flask import Flask, jsonify, request
from plaid import Configuration, ApiClient
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

configuration = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        "clientId": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
    }
)

api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@app.route('/create_link_token', methods=['GET'])
def create_link_token():
    request_data = LinkTokenCreateRequest(
        user=LinkTokenCreateRequestUser(client_user_id="user-123"),
        client_name="Smart Budget Tracker",
        products=[Products("transactions")],
        country_codes=[CountryCode('US')],
        language="en"
    )
    response = client.link_token_create(request_data)
    return jsonify(response.to_dict())

@app.route('/exchange_public_token', methods=['POST'])
def exchange_public_token():
    public_token = request.json.get('public_token')
    try:
        response = client.item_public_token_exchange({'public_token': public_token})
        access_token = response['access_token']
        return jsonify({'access_token': access_token})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/get_transactions', methods=['POST'])
def get_transactions():
    data = request.get_json()
    access_token = data.get('access_token')

    try:
        # Set date range
