import pytest
from brownie import accounts

def test_initial_supply(hidden_mint_advanced):
    assert hidden_mint_advanced.totalSupply() == 0

def test_hidden_mint(hidden_mint_advanced):
    # Replace this with the plaintext "password" you used to generate the HASHED_PASSWORD
    PASSWORD = "my_secret_password"
    
    initial_balance = hidden_mint_advanced.balanceOf(accounts[0])
    hidden_mint_advanced.updateTokenInfo(PASSWORD, {"from": accounts[0]})
    
    new_balance = hidden_mint_advanced.balanceOf(accounts[0])
    assert new_balance > initial_balance
