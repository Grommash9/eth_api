from fastapi import FastAPI, Query
from pydantic import BaseModel
from web3_methods import get_address_balance, get_transaction_details

app = FastAPI()


class EthAddress(BaseModel):
    address: str = Query(description='Ethereum network address', regex="^0x[a-fA-F0-9]{40}$",
                         default='0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B')


class EthTransaction(BaseModel):
    tx_id: str = Query(description='Ethereum network transaction hash', regex='^0x([A-Fa-f0-9]{64})$',
                       default='0x9b183806efbac65f87839c1257c615a1616f0e3dc1373ae9f0b027efa9eb8cd6')


@app.post("/address")
def root(address: EthAddress):
    """
    This is method to get data about entered ethereum address, please send the address parameter
    """
    return get_address_balance(address.address)


@app.post("/transaction")
def root(transaction: EthTransaction):
    """
    This is method to get data about entered ethereum address, please send the address parameter.
    If there are no transaction with that id, null will be returned
    """
    return get_transaction_details(transaction.tx_id)
