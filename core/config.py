from web3 import Web3
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

def pay_eth(from_acc,to_acc,pv,amt):
    to_acc="0xA3a417ccF2134515e433B5A2F38e26Efb1620A36"
    print(from_acc," to ",to_acc," : ",amt," ETH")
    context = {}
    if not web3.is_connected():
        context['err']= "Check Internet"
    
    balance = web3.eth.get_balance(from_acc)
    if balance <0:
        context['err']= "In suff blance"
    
   

    address1 = web3.to_checksum_address(from_acc)
    address2 = web3.to_checksum_address(to_acc)
    nonce = web3.eth.get_transaction_count(address1)
    tx = {
    'nonce':nonce,
    'to':address2,
    'value':web3.to_wei(float(amt), 'ether'),
    'gas':200000,
    'gasPrice':web3.to_wei('5000', 'gwei')
    }
    signed_tx = web3.eth.account.sign_transaction(tx,private_key=pv)
    try:
        tx_transation = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_script = web3.to_hex(tx_transation)
        tx_recipt = web3.eth.wait_for_transaction_receipt(tx_script)
        context['hash'] = tx_script
        context['recipt'] = tx_recipt
        context['transction'] = True
    except ValueError as e:
        context['err'] = str(e)
        context['transction'] = False

    return context