---
name: yield-opportunities
description: Comprehensive DeFi yield opportunity discovery and screening strategies
---

# Yield Opportunity Discovery Skill

A comprehensive skill for discovering and analyzing DeFi yield opportunities across multiple protocols and strategies with current rates and screening methodologies.

## Overview

This skill enables systematic discovery of yield opportunities across the DeFi ecosystem with current APY rates, risk assessment, and pool screening capabilities (筛选池子). It integrates with major data sources like DefiLlama and provides automated opportunity identification based on user-defined risk profiles.

## Core Capabilities

### Yield Discovery
- Real-time aggregation across 500+ protocols via DefiLlama API
- Current APY rates for all major DeFi strategies
- Cross-chain opportunity identification and comparison
- Risk-based opportunity categorization (conservative, moderate, aggressive)

### Pool Screening (筛选池子)
- Systematic protocol evaluation using multiple criteria
- TVL filtering with minimum thresholds
- Audit status verification for security
- Impermanent loss risk assessment
- Liquidity depth analysis for large deposits
- Single exposure filtering for stable strategies

### Strategy Analysis
- LSD/LRT yield optimization (stETH, ezETH, rsETH, Jito, Stader)
- Yield trading opportunities (Pendle, Gearbox)
- Leveraged farming strategies (high-risk, high-reward)
- Governance reward optimization (veCRV, CVX boosts)
- Stablecoin lending strategies (Aave, Sky, Ethena, Spark)

### Risk Management
- Multi-level risk categorization framework
- Smart contract due diligence integration
- Liquidation risk modeling
- Portfolio diversification analysis
- Historical performance tracking

## Workflow

### 1. Opportunity Discovery
Discover yield opportunities by filtering protocols based on TVL, audit status, and risk parameters using DefiLlama data API.

### 2. Pool Screening
Advanced filtering capabilities including TVL thresholds, audit verification, impermanent loss protection, and liquidity analysis.

### 3. Strategy Analysis
Comprehensive analysis of yield farming strategies with performance simulation and optimization recommendations.

## Data Sources Integration

### Primary APIs
- DefiLlama Yields: https://defillama.com/yields
- DefiLlama Protocol Data: https://defillama.com/protocols
- Aave API: https://aave-api-v2.aave.com/data
- Curve Subgraph: https://api.curve.fi/subgraphs/name/ethereum

### Protocol-Specific Analysis
- Aave: Real-time rates via AaveScan
- Curve: Weekly yield reports
- Pendle: Pool performance tracking
- Lido: Liquid staking dashboards
- Venus: BNB Chain lending rates
- Ethena: High-yield stablecoin strategies

## Usage

### Basic Discovery
```bash
# Discover all opportunities with moderate risk profile
yield-opportunities discover --risk-profile=moderate

# Conservative stablecoin-only opportunities
yield-opportunities discover --risk-profile=conservative --stablecoins-only --min-tvl=100000000

# Aggressive high-yield opportunities
yield-opportunities discover --risk-profile=aggressive --max-apy-filter=20

# Specific protocol analysis
yield-opportunities analyze --protocol=aave --asset=USDC
yield-opportunities analyze --protocol=pendle --asset=PT-eUSD
```

### Advanced Filtering
```bash
# Multi-chain analysis with specific criteria
yield-opportunities discover --chains=ethereum,arbitrum,polygon --min-tvl=50000000 --audited-only

# Include only liquid staking opportunities
yield-opportunities discover --lsd-only --min-apy=5

# Time-based analysis
yield-opportunities discover --timeframe=30d --sort-by=performance
```

## Installation

### Prerequisites
- Node.js 16+ or Python 3.8+
- Foundry (for blockchain interactions)
- API keys for DefiLlama, Aave, etc.

### Setup
```bash
# Install skill
npm install -g yield-opportunities

# Configure environment
export DEFILLAMA_API_KEY="your_api_key"
export AAVE_API_KEY="your_api_key"

# Initialize skill configuration
yield-opportunities init
```

## Risk Profiles

### Conservative
- TVL > $100M
- Audit status verified
- No impermanent loss
- Stablecoin preference

### Moderate  
- TVL > $50M
- Some risk accepted
- Mixed stablecoin and volatile assets

### Aggressive
- TVL > $10M
- Higher risk tolerance
- New protocols included
- High-yield focus

## Output Formats

### JSON Output
```json
{
  "opportunities": [
    {
      "protocol": "Sky Lending",
      "asset": "sUSDS", 
      "apy": "4.50%",
      "tvl": "$4.37B",
      "risk_level": "low",
      "chain": "ethereum"
    }
  ]
}
```

### Table Output
```
Protocol     Asset      APY     TVL       Risk
-----------  -------  ----     ---       ----
Sky Lending  sUSDS      4.50%   $4.37B    Low
Aave V3      USDC       3.25%   $747M     Low
Pendle       PT-eUSD     8.25%   $120M     Medium
```

## API Integration

### DefiLlama Functions
```python
# Fetch top yield opportunities
def get_top_opportunities(limit=10, min_tvl=1000000):
    return query_defillama(sort_by='apy', limit=limit, min_tvl_usd=min_tvl)

# Filter by specific attributes
def get_stablecoin_opportunities():
    return query_defillama(attribute='stablecoins', min_tvl_usd=50000000)

# Get LSD opportunities
def get_lsd_opportunities():
    return query_defillama(attribute='liquid_staking', sort_by='apy')
```

## Monitoring and Automation

### Alert System
Set up monitoring for yield changes and automatically rebalance based on predefined thresholds.

### Backtesting
Historical performance analysis to validate strategies before deployment.

## Security Considerations

- Contract verification before deployment
- Audit status checking
- Rug pull analysis for new protocols
- Liquidity lock verification
- Team and governance analysis

## Notes

- Always verify contract addresses directly on-chain
- Start with small test amounts for new protocols
- Consider gas costs in strategy optimization
- Diversification reduces overall portfolio risk
- Regular monitoring recommended for volatile markets

## Contributing

Contributions welcome! Please submit pull requests for additional features, protocol integrations, or improvements to the screening algorithms.

## License

MIT License
