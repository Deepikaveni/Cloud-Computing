import json
import boto3

# Load response from Plaid
with open('transactions_response.json', 'r') as f:
    plaid_data = json.load(f)

# Extract only transactions
transactions = plaid_data.get('transactions', [])

# ✅ S3 setup
s3 = boto3.client('s3')
bucket_name = 'budget-tracker-bucket-690'

s3.put_object(
    Bucket=bucket_name,
    Key='raw/plaid/transactions_response.json',
    Body=json.dumps(plaid_data)
)

# ✅ DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UseraTransactions')

for txn in transactions:
    try:
        table.put_item(Item={
            'userID': 'user123',
            'transactionID': txn['transaction_id'],
            'amount': float(txn['amount']),
            'category': txn['category'][0] if txn.get('category') else 'Unknown',
            'merchant': txn.get('name', 'Unknown'),
            'date': txn['date'],
            'fraud_flag': 0
        })
    except Exception as e:
        print(f"Error inserting {txn['transaction_id']}: {str(e)}")
