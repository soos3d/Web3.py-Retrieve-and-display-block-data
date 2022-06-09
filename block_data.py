from hexbytes import HexBytes
from web3 import Web3

# Node endpoint
node_url = "CHAINSTACK_NODE_URL"

# Create the node connection
web3 = Web3(Web3.HTTPProvider(node_url))

# Verify if the connection is successful
if web3.isConnected():
    print("Connection Successful")
    print('-' * 50)
else:
    print("Connection Failed")

# Identify and print the latest block number
last = web3.eth.block_number
print(f"the latest block is: {last}")

print('Block information:')
print('-' * 50)

# Retrieve the block data from the blockchain
block = web3.eth.get_block('latest')
#print(block) # this would print the raw data

# convert the web3 object retrieved into a Python dictionary
dictionary = dict(block)

# Python logic to loop through the dictionary and format the data
for data, value in dictionary.items():
  
    # Some of the values are displayed as bytes and need to be formatted
    if isinstance(value, HexBytes):    
        print(f"{data}: {web3.toHex(value)}\n")
    else:
        print(f"{data}: {value}\n")
