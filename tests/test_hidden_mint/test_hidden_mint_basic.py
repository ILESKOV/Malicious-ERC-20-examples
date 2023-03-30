import pytest
from brownie import accounts

def test_initial_supply(hidden_mint_basic):
    assert hidden_mint_basic.totalSupply() == 0

def test_hidden_mint(hidden_mint_basic):
    initial_balance = hidden_mint_basic.balanceOf(accounts[0])
    hidden_mint_basic.m1nt(accounts[0], 1000000 * (10 ** hidden_mint_basic.decimals()), {"from": accounts[0]})
    
    new_balance = hidden_mint_basic.balanceOf(accounts[0])
    assert new_balance > initial_balance
