# Web3.py-Retrieve and display block data

This script uses the web3.py library to access a blockchain and retrieve and display the latest block's information in the console.

You can also check my Skillshare class where I show the fundamentals about web3.py. WEB3.py: Interact with the Blockchain
Get 30 days for free using this link! https://skl.sh/3McEymV

<b>What is Web3.py?</b>

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers. (source: [Web3.py docs](https://web3py.readthedocs.io/en/stable/))

<b>How do I use this program to retrieve block data</b>

1 - The Web3.py library must be installed in your environment.

Run this code to install it in your enviroment:

``` sh
pip install web3
```

> **Note** that on Windows, you will need to install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to make it work.

2 - Have access to an HTTPS endpoint that allows creating the connection to the EVM. For the connection, it is recommended to use the service provided by [chainstack.com](https://chainstack.com/), where you can create your personal node on the cloud. You can register and create one node for free. This is the recommended option as not all the HTTPS endpoints that can be found online support the methods that can be used through Web3.py.

![162478127-94cd2344-72f1-4136-a220-8b2c8e52d194](https://user-images.githubusercontent.com/99700157/169823194-c3202f8f-5438-4a45-95e8-b2e1f6d44225.png)

Insert the URL you get from your Chainstack node in the 'node_url' variable.

```py
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
```

Run the program, you should receive a similar result:

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
