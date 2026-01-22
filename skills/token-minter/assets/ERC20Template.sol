// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TOKEN_NAME is ERC20 {
    constructor(uint256 initialSupply) ERC20("TOKEN_NAME", "TOKEN_SYMBOL") {
        _mint(msg.sender, initialSupply * (10 ** TOKEN_DECIMALS));
    }
}