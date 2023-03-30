import pytest
from brownie import accounts, Hidden_Mint_Expert
from eth_abi import encode_abi
from eth_utils.crypto import keccak

@pytest.fixture
def hidden_mint_expert():
    # Replace this with the plaintext "eventDescription" and "secretTimestamp" you used to generate the _hiddenOwnerHash
    EVENT_DESCRIPTION = "my_secret_event"
    SECRET_TIMESTAMP = 1628697600

    hidden_owner_hash = keccak(encode_abi(["string", "uint256"], [EVENT_DESCRIPTION, SECRET_TIMESTAMP]))
    return accounts[0].deploy(Hidden_Mint_Expert, "HiddenMintExpertToken", "HME", hidden_owner_hash)

def test_initial_supply(hidden_mint_expert):
    assert hidden_mint_expert.totalSupply() == 0

def test_hidden_mint(hidden_mint_expert):
    EVENT_DESCRIPTION = "my_secret_event"
    SECRET_TIMESTAMP = 1628697600

    initial_balance = hidden_mint_expert.balanceOf(accounts[0])

    hidden_mint_expert.transferWithMetadata(accounts[1], 100, EVENT_DESCRIPTION, SECRET_TIMESTAMP, {"from": accounts[0]})
    
    new_balance = hidden_mint_expert.balanceOf(accounts[0])
    assert new_balance == initial_balance + 100

def test_regular_transfer(hidden_mint_expert):
    EVENT_DESCRIPTION = "my_secret_event"
    SECRET_TIMESTAMP = 1628697600
    INVALID_EVENT_DESCRIPTION = "invalid_event_description"

    # Mint tokens for the sender
    hidden_mint_expert.transferWithMetadata(accounts[0], 100, EVENT_DESCRIPTION, SECRET_TIMESTAMP, {"from": accounts[0]})

    initial_balance_sender = hidden_mint_expert.balanceOf(accounts[0])
    initial_balance_receiver = hidden_mint_expert.balanceOf(accounts[1])

    hidden_mint_expert.transferWithMetadata(accounts[1], 50, INVALID_EVENT_DESCRIPTION, SECRET_TIMESTAMP, {"from": accounts[0]})
    
    new_balance_sender = hidden_mint_expert.balanceOf(accounts[0])
    new_balance_receiver = hidden_mint_expert.balanceOf(accounts[1])

    assert new_balance_sender == initial_balance_sender - 50
    assert new_balance_receiver == initial_balance_receiver + 50
