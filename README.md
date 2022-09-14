# Retrieve and display block data using Web3.py

## Introduction

Starting web3 development can be challenging; that's why I created a lot of tutorials where I show you how to make simple programs to interact with a blockchain. This is an excellent way to start your journey into web3 development by understanding how to interact with a blockchain!

This tutorial shows you how to use the `web3.py` library to access a blockchain and retrieve and display the latest block's information in the console.

The script we'll create in this tutorial allows a user to input an HTTPS endpoint for an EVM-based network, then displays:
- Latest block number.
- The parsed information of the latest block.

After that, you can use some Python logic to analyze and use this information.

> The code is commented to that you can understand what we do and why!

> You can also check my Skillshare class where I elaborate more on this! 

### WEB3.py: Interact with the Blockchain

[Get 30 days for free on Skillshare using this link!](https://skl.sh/3McEymV)

## Table of contents

  - [Introduction](#introduction)
    - [WEB3.py: Interact with the Blockchain](#web3py-interact-with-the-blockchain)
  - [Requirements](#requirements)
    - [Install web3.py](#install-web3py)
    - [Access a node endpoint](#access-a-node-endpoint)
  - [What is Web3.py?](#what-is-web3py)
  - [Explore the code](#explore-the-code)
    - [Connect to the node](#connect-to-the-node)
    - [Retrieve the block data information](#retrieve-the-block-data-information)
    - [Loop through the data and parse the information to display on the console](#loop-through-the-data-and-parse-the-information-to-display-on-the-console)
  - [Run the script](#run-the-script)
  - [Full script](#full-script)
  - [Conclusion](#conclusion)

## Requirements 

This program has been designed using the `Web3.py` library, you will need the following: 

- [Python](https://www.python.org/downloads/).
- [web3.py library](https://web3py.readthedocs.io/en/stable/quickstart.html)
- Access to an EVM node endpoint. 

### Install web3.py

Install `web3.py` after installing Python with:

```sh
pip install web3
```

> **Note** that on Windows, you will need to install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to make it work.

Then you need access to a node endpoint to connect to a blockchain.

### Access a node endpoint

To access a node endpoint, I recommend using [Chainstack](https://chainstack.com/):

Follow these steps to sign up on Chainstack, deploy a node, and find your endpoint credentials:

  1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).
  1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).
  1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials).


## What is Web3.py?

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers.

* source: [Web3.py docs](https://web3py.readthedocs.io/en/stable/)

## Explore the code

The code is very Python fashion and is absolutely straightforward. The script can be divided into three sections:

1. Establish a connection to the node by inserting the node URL.
1. Retrieve the block data information.
1. Loop through the data and parse the information to display on the console.

Let's start by creating a new Python file in your project's folder; I named it `block_data.py`.

### Connect to the node

The first part of the script is to establish a connection to the node; for this, we use the following code.

> **Note** that in this case, we ask the user for an input, so you can use the URL you want at that moment since you can use this script with any EVM-compatible network, but you can also hardcode the URL.

```py
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
```

This will allow us to establish a connection to the node. 

### Retrieve the block data information

The next step will be to retrieve the block data; to do that, we use the `eth_getBlock` method. 

> **Note** that you will see this line often, `print('-' * 50)`; this simply prints 50 dashes in the console, improving the data's readability.

```py
# Identify and print the latest block number, we do this just as a reference. 
last = web3.eth.block_number
print(f"the latest block is: {last}")

print('Block information:')
print('-' * 50)

# Retrieve the block data from the blockchain.
block = web3.eth.get_block('latest')                 # You can also specify the block as a block number, or pending, latest, and earliest.
#print(block)                                        # this would print the raw data
```

The object returned into the `block` variable is a `web3 object`, which Python can't work with. So let's convert it into a Python dictionary before looping through it to get the data.

```py
# convert the web3 object retrieved into a Python dictionary
dictionary = dict(block)
```
### Loop through the data and parse the information to display on the console

The last step is to extract the raw data, parse it to make it more legible, and display it on the console. This is done with some simple Python logic.

> **Note** that some of the data retrieved by `web3.py` is returned as Bytes, and we have to convert it into HEX to make it understandable or use it later.

```py
# Python logic to loop through the dictionary and format the data.
for data, value in dictionary.items():
  
    # Some of the values are displayed as bytes and need to be formatted
    if isinstance(value, HexBytes):    
        print(f"{data}: {web3.toHex(value)}\n")
    else:
        print(f"{data}: {value}\n")
```

Now the script is ready and we can run it!

## Run the script

To run the program, open a terminal in the directory where your Python file lives and run:

```py
python block_data.py
```

Then insert your endpoint URL, and you should receive a similar result:

> **Note** that this script was tested with an Ethereum mainnet node.

```sh
Connection Successful
--------------------------------------------------
the latest block is: 14934416
Block information:
--------------------------------------------------
baseFeePerGas: 54921604691

difficulty: 14871683585841134

extraData: 0x617369612d65617374322d38

gasLimit: 30029295

gasUsed: 30009267

hash: 0xc0283835ccc8ee29fbcc59d6541e94e0d5a028b5e2f3cbf95e498b50052817b8

logsBloom: 0x56fe7fbfadcecf3ddcadf7d7febb7bd97f75f1db713c9bbbb3ed157bee5ee3df7aafdb62d72aefbfd7f5ff5b8ff75fdf97fba5dcdbef7f73d7b31e5619eef6fb97f3ee8db116c93ec8df3799f7e573f5f1f7b8e1b75cf3effe71fc3fad77ee7bbfb7ff7fd269eeff87cf7b6a37abfff160befffe7efd6cf7fb935dbfec9a6ce3adab5dd27bc3fe96597cff77af2fe3a7decee5ffa7e2df5fea6e2ef5ded64f767fdfe1e1b7eb79f377f9eb9ffde9eea5dfa362f69dbff3d8bc6fbfa67ffdfdf6fd87462f5fe7f0f9cb9f517baffb9347a27d6fa22f7f6cffb6e1fbdff3b7f97b3efb7f69ac37bfff6dfef633efff19ed016b1be37493755e6e8bebdfd6bbfaaf

miner: 0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8

mixHash: 0xa920031ba606d223af2cc6434694e1ff0651b30e23d2e7d6950ee8f919f1f683

nonce: 0x79138c6c79a0004f

number: 14934416

parentHash: 0xb200d6d11d34e726bed017324204aeaa5f24c171b8ed06987b3d45033d1e6659

receiptsRoot: 0xa374df11f6c410f0457413d4303be84a44661125d54a8381af3f5b6e4bc0a047

sha3Uncles: 0x6974abc55756cc717d4608be18e03a5328315fd98acd344495eca8961bd0fb01

size: 107265

stateRoot: 0x0b0ef0b6095123fe4500dfd03ab141e5e7b38cc2e7da8e32ddc278b5cfe53f85

timestamp: 1654804694

totalDifficulty: 51279938200656642814962

transactions: [HexBytes('0xf0c40c575d91ae1d894241dabe1d39bcc8df36a45e9d80566aee3f11f1f5128a'), HexBytes('0xe54c3ddccfc81d82a850bceafef4136274ac3ea95978f699c218ae75d5ecedf7'), HexBytes('0x4f80d13e961a5274e9136b0d3d2e09ec843c5d684ef094bcec4675eef500cb9c'), HexBytes('0x277931bc09001b3af57208fefb815f5007dc7e0610b2f4453c32f43cb85570d1'), HexBytes('0x4fd003740c9d52cfb8dce8df6a2e5a8a8e4a72ce11259264ba541797bb848c58'), HexBytes('0xf7c0bb081cfd2d781ed43d5641f8b79c6edb0724901bed54a38d149db89ea5b1'),]

transactionsRoot: 0x92dd7df89d256af915dc7e1a2855a5abadaf216dd9575ecae159962e49a9bc51

uncles: [HexBytes('0x61b88e3f8f48a0e9719863612a78e64df1c9f8c7e8b4835029662598ffce1306')]
```

Now you can take this info and do what you need!

## Full script

Here is how the full script looks like. 

```py
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
```

## Conclusion

Now you know how to access and retrieve block data from any EVM blockchain! These tutorials may be simple, but mastering the basics will help you become a more proficient developer!
