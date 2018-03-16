# -*- coding: utf-8 -*-
from web3 import Web3,HTTPProvider

def lambda_handler(event, context):
    web3 = Web3(HTTPProvider('http://YOUR_ETH_NODE:8540'))
    blockNumber=web3.eth.blockNumber
    print(blockNumber)
    return blockNumber
