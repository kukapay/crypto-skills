# ERC20 Token Standard

## Overview
ERC20 is the technical standard for fungible tokens on the Ethereum blockchain. It defines a common interface that allows tokens to be exchanged, transferred, and used across different applications.

## Required Functions
- `totalSupply()`: Returns the total token supply
- `balanceOf(address)`: Returns the balance of a specific address
- `transfer(address, uint256)`: Transfers tokens to another address
- `transferFrom(address, address, uint256)`: Transfers tokens on behalf of another address
- `approve(address, uint256)`: Approves an address to spend tokens
- `allowance(address, address)`: Returns the remaining allowance

## Events
- `Transfer(address indexed from, address indexed to, uint256 value)`
- `Approval(address indexed owner, address indexed spender, uint256 value)`

## Deployment Requirements
- Solidity ^0.8.0
- OpenZeppelin ERC20 contract
- Foundry for compilation and deployment

## Network Considerations
- Mainnet: Ethereum mainnet
- Testnets: Sepolia, Goerli, Mumbai (Polygon), etc.
- Ensure sufficient gas for deployment