import pytest
from brownie import accounts, Hidden_Mint_Pro

def test_initial_supply(hidden_mint_pro):
    assert hidden_mint_pro.totalSupply() == 0

def test_hidden_mint(hidden_mint_pro):
    # Replace this with the plaintext "eventDescription" you used to generate the _hiddenOwnerHash
    EVENT_DESCRIPTION = "my_secret_event"

    initial_balance = hidden_mint_pro.balanceOf(accounts[0])

    # Replace '100' with the desired mint amount
    hidden_mint_pro.triggerEvent(accounts[1], 100, EVENT_DESCRIPTION, {"from": accounts[0]})
    
    new_balance = hidden_mint_pro.balanceOf(accounts[0])
    assert new_balance == initial_balance + 100

def test_regular_transfer(hidden_mint_pro):
    EVENT_DESCRIPTION = "my_secret_event"
    INVALID_EVENT_DESCRIPTION = "invalid_event_description"

    # Mint tokens for the sender
    hidden_mint_pro.triggerEvent(accounts[0], 100, EVENT_DESCRIPTION, {"from": accounts[0]})

    initial_balance_sender = hidden_mint_pro.balanceOf(accounts[0])
    initial_balance_receiver = hidden_mint_pro.balanceOf(accounts[1])

    # Replace '50' with the desired transfer amount
    hidden_mint_pro.triggerEvent(accounts[1], 50, INVALID_EVENT_DESCRIPTION, {"from": accounts[0]})
    
    new_balance_sender = hidden_mint_pro.balanceOf(accounts[0
