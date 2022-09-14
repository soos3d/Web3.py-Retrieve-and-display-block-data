from web3 import Web3                            # Import the web3 library at the top.
from hexbytes import HexBytes                    # Import the hexbytes to convert bytes into HEX.

node_url = input('Insert your Node URL: ')       # Accepts the user node URL.
web3 = Web3(Web3.HTTPProvider(node_url))         # Establish connection to the node.

# Verify if the connection is successful. This is optional, but it's nice to notify the user.
if web3.isConnected():                                                          
    print('Connection Successful')
    print('-' * 50)
else:
    print('Connection Failed')

# Identify and print the latest block number
last = web3.eth.block_number
print(f"the latest block is: {last}")

print('Block information:')
print('-' * 50)

# Retrieve the block data from the blockchain
block = web3.eth.get_block('latest')                # You can also specify the block as a block number, or pending, latest, and earliest.
#print(block)                                       # this would print the raw data

# convert the web3 object retrieved into a Python dictionary
dictionary = dict(block)

# Python logic to loop through the dictionary and format the data
for data, value in dictionary.items():
  
    # Some of the values are displayed as bytes and need to be formatted
    if isinstance(value, HexBytes):    
        print(f"{data}: {web3.toHex(value)}\n")
    else:
        print(f"{data}: {value}\n")
