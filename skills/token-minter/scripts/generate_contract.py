#!/usr/bin/env python3
import sys


def generate_erc20_contract(name, symbol, decimals, initial_supply):
    template = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract {name} is ERC20 {{
    constructor(uint256 initialSupply) ERC20("{name}", "{symbol}") {{
        _mint(msg.sender, initialSupply * (10 ** {decimals}));
    }}
}}"""
    return template.format(name=name, symbol=symbol, decimals=decimals)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python generate_contract.py <name> <symbol> <decimals> <initial_supply>"
        )
        sys.exit(1)

    name = sys.argv[1]
    symbol = sys.argv[2]
    decimals = int(sys.argv[3])
    initial_supply = int(sys.argv[4])

    contract_code = generate_erc20_contract(name, symbol, decimals, initial_supply)
    print(contract_code)
