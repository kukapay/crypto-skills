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

### Market Sentiment
A comprehensive tool for analyzing cryptocurrency market sentiment by aggregating news from popular RSS feeds and performing sentiment analysis. Supports:

- RSS feed aggregation from multiple crypto news sources
- Automated sentiment classification (positive/negative/neutral)
- Market sentiment scoring (range: -1 to +1)
- Evidence-based explanations with article breakdowns

This skill helps AI agents assess overall market mood for trading decisions, research, and trend monitoring.

### Meme Scout
A comprehensive tool for scouting trending meme coins on DEX platforms like DexScreener. Supports:

- Discovering trending tokens with multiple timeframes (5m, 1h, 6h, 24h)
- Analyzing price movements, volume data, and risk assessments
- Risk checking capabilities for specific tokens on Solana and other chains

This skill enables AI agents to identify and evaluate trending meme coins for trading and research purposes.

### Token Minter
A comprehensive tool for generating, building, and deploying custom ERC20 tokens on EVM networks. Supports:

- Custom token parameters (name, symbol, decimals, initial supply)
- Automatic Solidity contract generation using OpenZeppelin standards
- Foundry project setup and dependency management
- Contract compilation and deployment to various networks
- Support for testnets like Sepolia

This skill enables AI agents to create and deploy custom ERC20 tokens with full control over token parameters and deployment targets.

## Installation

Install these skills using the Skills CLI:


```bash
npx skills add kukapay/crypto-skills
```

Or you can install a single skill:


```bash
npx skills add kukapay/crypto-skills --skill "evm-swiss-knife"
```

This command will download and configure the crypto skills for your AI agent.

For more information about the Skills CLI, visit [https://skills.sh/docs/cli](https://skills.sh/docs/cli).

## Future Expansion

This repository is actively maintained and will continue to expand with additional crypto-related skills, including:

- DeFi protocol interactions
- Wallet management utilities
- Cross-chain bridge operations
- And more blockchain utilities


## Contributing

Contributions are welcome! If you have ideas for new crypto skills or improvements to existing ones, please open an issue or submit a pull request.

## License

MIT License

