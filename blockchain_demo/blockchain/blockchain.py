from flask import Flask, render_template
from time import time

class Blockchain:
	def __init__(self):
		self.transactions = []
		self.chain = []
		#create the genesis block
		self.create_block(0, '00') 
		
		
		
	def create_block(self, nonce, previous_hash):
		"""
		Add a block of transactions to the blockchain
		
		"""
		#create dictionary
		block = {'block_number': len(self.chain) + 1,
				'timestamp': time(),
			'transactions': self.transactions,
			'nonce': nonce,
			'previous_hash': previous_hash
		}
		
		#empty transactions cuz already added
		self.transactions = []
		self.chain.append(block)
		
		
		
#instantiate the blockchain
blockchain = Blockchain()

#instantiate the Node
app = Flask(__name__)


#front functionalityr
#endpoints
@app.route('/')

def index():
	return render_template('./index.html')

if __name__ == '__main__':
	from argparse import ArgumentParser
	
	parser = ArgumentParser()
	parser.add_argument('-p', '--port', default=5001, type=int, help="port to listen to")
	args = parser.parse_args()
	port = args.port
	
	#host = local host
	app.run(host='127.0.0.1', port=port, debug=True)