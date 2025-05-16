# ☁️ Smart Budget Tracker – Cloud-Based Transaction Uploader

This is a cloud-integrated web application that fetches Plaid transaction data from AWS S3, processes and cleans it using Python, and uploads it to DynamoDB. It includes a Flask-based backend and a basic HTML frontend.

---

## 📁 Project Structure

```
.
├── app.py                           # Flask backend to process and upload data
├── templates/
│   └── index.html                   # Frontend HTML file
├── static/                          # (Optional) Static files like CSS or JS
├── plaid_transactions_cleaned.csv  # Output cleaned CSV
└── README.md                        # Project documentation
```

---

## 🧰 Requirements

- Python 3.9+
- Flask
- pandas
- boto3
- AWS IAM user with S3 and DynamoDB access
- VS Code with Live Server extension (for frontend)

---

## ⚙️ Setup Instructions

### 1. 🐍 Backend Setup (app.py)

1. Install dependencies:

```bash
pip install flask boto3 pandas
```

2. Update the following variables in `app.py`:

```python
bucket_name = 'your-s3-bucket-name'
file_key = 'your-plaid-file.json'
region_name = 'your-aws-region'
table_name = 'UserTransactions'
aws_access_key_id = 'your-access-key'
aws_secret_access_key = 'your-secret-key'
```

3. Run the backend server:

```bash
python app.py
```

Flask will start at:  
➡️ http://127.0.0.1:5000

---

### 2. 🌐 Frontend Setup (index.html)

1. Open the folder in **Visual Studio Code**
2. Right-click `templates/index.html` and select **"Open with Live Server"**
3. The frontend will open at:  
➡️ http://127.0.0.1:5500/templates/index.html

Make sure `app.py` is running for backend interaction.

---

## ✅ Example Workflow

```bash
# 1. Start Flask backend
python app.py

# 2. Open frontend via Live Server
# 3. Watch terminal for progress/logs
```

---

## 📌 Notes

- `Decimal(str(amount))` is used to meet DynamoDB's number type requirement
- You can switch to `batch_writer()` for faster bulk inserts
- `userID` is static (e.g., 'user123') in this version

---

## 🚀 Future Enhancements

- [ ] Dynamic user authentication
- [ ] Plaid API integration
- [ ] Transaction viewer dashboard
- [ ] Export from DynamoDB to CSV

---

## 📜 License

This project is licensed under the MIT License.
