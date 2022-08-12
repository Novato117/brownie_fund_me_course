from brownie import FundMe, accounts
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print("funding")
    fund_me.found({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
