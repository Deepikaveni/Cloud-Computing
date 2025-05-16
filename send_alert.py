import boto3

# Initialize the SNS client
sns = boto3.client('sns', region_name='us-east-1')

# Correct Topic ARN
topic_arn = 'arn:aws:sns:us-east-1:770912375813:fraud_alert'

fraud_flag = -1  # Example condition

if fraud_flag == -1:
    sns.publish(
        TopicArn=topic_arn,
        Message='⚠️ A suspicious transaction was detected!',
        Subject='🚨 Fraud Alert'
    )
    print("🚨 Fraud alert sent to user via SNS.")
else:
    print("✅ No fraud detected.")

topic_arn = 'arn:aws:sns:us-east-1:770912375813:fraud_alert'
