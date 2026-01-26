# Crypto Skills

This repository provides a collection of specialized AI agent skills focused on cryptocurrency and blockchain operations. These skills enhance AI agents with the ability to interact with various blockchain networks, query market data, and perform crypto-related tasks.

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

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "evm-swiss-knife"
```

### Market Sentiment
A comprehensive tool for analyzing cryptocurrency market sentiment by aggregating news from popular RSS feeds and performing sentiment analysis. Supports:

- RSS feed aggregation from multiple crypto news sources
- Automated sentiment classification (positive/negative/neutral)
- Market sentiment scoring (range: -1 to +1)
- Evidence-based explanations with article breakdowns

This skill helps AI agents assess overall market mood for trading decisions, research, and trend monitoring.

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "market-sentiment"
```

### Meme Scout
A comprehensive tool for scouting trending meme coins on DEX platforms like DexScreener. Supports:

- Discovering trending tokens with multiple timeframes (5m, 1h, 6h, 24h)
- Analyzing price movements, volume data, and risk assessments
- Risk checking capabilities for specific tokens on Solana and other chains

This skill enables AI agents to identify and evaluate trending meme coins for trading and research purposes.

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "meme-scout"
```

### Token Minter
A comprehensive tool for generating, building, and deploying custom ERC20 tokens on EVM networks. Supports:

- Custom token parameters (name, symbol, decimals, initial supply)
- Automatic Solidity contract generation using OpenZeppelin standards
- Foundry project setup and dependency management
- Contract compilation and deployment to various networks
- Support for testnets like Sepolia

This skill enables AI agents to create and deploy custom ERC20 tokens with full control over token parameters and deployment targets.

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "token-minter"
```

### Trading Strategist
A comprehensive tool for generating trading strategies for cryptocurrencies by combining Binance market data, technical analysis indicators, and market sentiment analysis. Supports:

- Real-time price and historical data from Binance API
- Technical indicators (SMA, EMA, RSI, Bollinger Bands, MACD, Stochastic)
- Integration with market sentiment scores
- Strategy recommendations with entry/exit points and risk management
- Support for major cryptocurrencies like BTC, ETH, BNB

This skill enables AI agents to provide data-driven trading advice and strategy analysis.

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "trading-strategist"
```

### Yield Opportunities
A comprehensive tool for finding and analyzing DeFi yield opportunities across protocols, chains, and asset types. Supports:

- Parallel research workflows using librarian agents for comprehensive data collection
- Staking analysis (native delegation, liquid staking, restaking)
- Lending protocol yield comparison (Aave, Venus, Alpaca, etc.)
- Liquidity pool farming analysis (Uniswap, PancakeSwap, Curve, etc.)
- Yield aggregator vault tracking (Beefy, Yearn, Autofarm, ACryptoS)
- Cross-chain bridging yield opportunities
- Risk assessment framework with 8-category scoring system
- Protocol security checklist and due diligence
- Automated scripts for fetching and comparing yields

This skill enables AI agents to provide comprehensive DeFi yield research with current APY/APR data, risk analysis, and tailored recommendations across multiple blockchains (Ethereum, BSC, Solana, Arbitrum, Optimism, Polygon, etc.).

**Install:**
```bash
npx skills add kukapay/crypto-skills --skill "yield-opportunities"
```

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

