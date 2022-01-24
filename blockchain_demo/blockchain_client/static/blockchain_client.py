from flask import Flask, render_template

class Transaction:
	def __init__(self, sender_address, sender_private_key, recipient_address, value):
		self.sender_address = sender_address
		self.sender_private_key = sender_private_key
		self.recipient_address = recipient_address
		self.value = value
		

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/make/transaction')
def make_transaction():
	return render_template('make_transaction.html')

@app.route('/view/transactions')
def view_transactions():
	return render_template('view_transactions.html')