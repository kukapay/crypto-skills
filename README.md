# Crypto Skills

This repository provides a collection of specialized AI agent skills focused on cryptocurrency and blockchain operations. These skills enhance AI agents with the ability to interact with various blockchain networks, query market data, and perform crypto-related tasks.

## Current Skills

### EVM Swiss Knife
A comprehensive tool for interacting with Ethereum Virtual Machine (EVM)-compatible blockchains using Foundry's `cast` command-line tool. Supports:

- Account balance queries
- Contract function calls (read/write)
- Transaction sending
- Blockchain inspection
- Contract deployment
- Data decoding

This skill enables AI agents to perform low-level blockchain operations across multiple EVM networks like Ethereum, Polygon, BNB Smart Chain, and more.

## Installation

Install these skills using the Skills CLI:


```bash
npx skills add kukapay/crypto-skills
```

Or you can install a sinle skill:


```bash
npx skills add kukapay/crypto-skills --skill "evm-skill-knife"
```

This command will download and configure the crypto skills for your AI agent.

For more information about the Skills CLI, visit [https://skills.sh/docs/cli](https://skills.sh/docs/cli).

## Future Expansion

This repository is actively maintained and will expand with additional crypto-related skills in the near future, including:

- Price tracking and market analysis tools
- DeFi protocol interactions
- Wallet management utilities
- Cross-chain bridge operations
- And more blockchain utilities


## Contributing

Contributions are welcome! If you have ideas for new crypto skills or improvements to existing ones, please open an issue or submit a pull request.

## License

MIT License

