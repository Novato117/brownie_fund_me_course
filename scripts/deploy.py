from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_addres = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_addres = MockV3Aggregator[-1].address

    # account = get_account()
    print(account.balance)
    fund_me = FundMe.deploy(
        price_feed_addres,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me  # para testing


def main():
    deploy_fund_me()
