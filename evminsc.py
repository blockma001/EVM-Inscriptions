# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 01:00:18 2023

@author: Stanley Ma
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:39:24 2023

@author: Stanley Ma
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 01:40:20 2023

@author: Stanley Ma
"""

from web3 import Web3


def trans_data(sen,cont,chainid,nonce,data,private_key):
    price = int(web3.eth.gasPrice*1.2)
    txn = {
        'from': sen,
        'to': cont,
        'chainId': chainid,
        'nonce': nonce,
        'gas': 50000,
        'value': 0,
        'gasPrice': price,
        'data': data,
    }
    gas = int(int(web3.eth.estimateGas(txn))*1.15)
    txn1 = {
        'from': sen,
        'to': cont,
        'chainId': chainid,
        'nonce': nonce,
        'gas': gas,
        'value': 0,
        'gasPrice': price,
        'data': data,
    }
    signed_txn = web3.eth.account.sign_transaction(txn1, private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return str(web3.toHex(tx_token))

def ks(add2,private2,start):
    sen = web3.toChecksumAddress(add2)
    pri = private2
    nonce = web3.eth.get_transaction_count(sen)
    for i in range(0,int(start)):
        try:
            balance = web3.eth.get_balance(sen)
            humanReadable = web3.fromWei(balance, 'ether')
        except Exception as e:
            print('第'+str(i+1)+'个号，错误原因：'+str(e)+'，跳过。')
            continue
        print('第'+str(i+1)+'个号，余额'+str(humanReadable)+' AVAX')
        
        if humanReadable>0:
            
            try:
                b = trans_data(sen,sen,chainid,nonce,data0,pri)
                print('第'+str(i+1)+'个号，'+'哈希：'+str(b))
                nonce+=1
            except Exception as e:
                print('第'+str(i+1)+'个号，错误原因：'+str(e)+'，跳过。')
                continue
            print('第'+str(i+1)+'个号，全部完成')
        else:
            print('第'+str(i+1)+'个号，余额不足.')
    print('全部完成！')

aa = input("add:")
bb = input("private:")
cc = input("start:")
dd = input("rpc:")
ee = input("chain id:")
ff = input("data:")

rpc = dd
web3 = Web3(Web3.HTTPProvider(rpc))
chainid = int(ee)
data0 = ff

ks(aa,bb,cc)