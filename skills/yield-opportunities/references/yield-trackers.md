# Yield Tracking Tools and APIs

This comprehensive guide covers tools, APIs, and dashboards for tracking DeFi yields in real-time.

## Primary Yield Aggregators (Best Place to Start)

### DefiLlama Yields
**URL:** https://defillama.com/yields
**Coverage:** 14,149 pools across 495 protocols on 110 chains
**Update Frequency:** Daily

**Features:**
- Filter by chain (Ethereum, BSC, Arbitrum, Solana, etc.)
- Filter by token (ETH, BTC, BNB, stablecoins, etc.)
- Filter by protocol (Aave, Compound, PancakeSwap, etc.)
- Filter by APY range
- Filter by TVL range
- Filter by category (lending, staking, LP, single asset)
- Sort by APY, TVL, pool name
- View pool details (token, chain, protocol, APY, TVL)
- 30-day APY mean
- Reputation score (protocol risk indicator)

**API Endpoints:**
```bash
# All pools
GET https://yields.llama.fi/pools

# Pools by chain
GET https://yields.llama.fi/pools?chain=ethereum

# Pools by token
GET https://yields.llama.fi/pools?token=bnb

# Pool details (chart history)
GET https://yields.llama.fi/chart/{pool}

# Borrow APY
GET https://yields.llama.fi/borrow

# LSD rates (liquid staking)
GET https://yields.llama.fi/lsdRates
```

**Pros:**
- Most comprehensive coverage
- Open-source and free
- Daily updates
- Multiple filter options
- API access for automation
- Reputation scores included

**Cons:**
- Some newer protocols may not be listed
- APYs are delayed (not real-time)

---

### Vaults.fyi
**URL:** https://vaults.fyi/complete-list-of-defi-vaults-yields-updated-daily/
**Coverage:** 500+ vaults across 50+ protocols
**Update Frequency:** Daily

**Features:**
- Yield aggregator vaults only (Beefy, Yearn, etc.)
- Daily updated APYs
- Protocol filtering
- Chain filtering
- Token filtering
- On-chain data transparency

**Pros:**
- Specialized for vaults/yield aggregators
- Daily updates
- Focus on auto-compounding strategies
- Transparent APY calculation methodology

**Cons:**
- Only covers vaults, not direct lending/staking
- Smaller dataset than DefiLlama

---

### DexLender
**URL:** https://dexlender.com/
**Coverage:** Stablecoin lending rates across chains
**Update Frequency:** Live (as of page load date)

**Features:**
- Stablecoin APYs (USDC, USDT, DAI, etc.)
- Multi-chain support
- Current base APY
- Protocol comparison
- Sort by highest APY

**Pros:**
- Great for stablecoin yield comparison
- Real-time rates
- Simple interface

**Cons:**
- Only stablecoins
- Only lending protocols (not staking/LP)

---

### CoinMarketCap Yield
**URL:** https://coinmarketcap.com/yield/
**Coverage:** Multi-asset, DeFi and CeFi options
**Update Frequency:** Periodic

**Features:**
- Yield type categorization (Earn, Staking, etc.)
- Provider type (DeFi/CeFi)
- Net APY display
- Multiple assets supported
- FAQ section on yield mechanics

**Pros:**
- Covers both DeFi and CeFi
- Easy to understand interface
- Good for beginners

**Cons:**
- Less comprehensive than DefiLlama
- Not real-time for many entries
- Some data may be outdated

---

## Chain-Specific Dashboards

### Ethereum
- **DefiPulse:** https://defipulse.com/ (legacy but still useful)
- **Curve.fi:** https://curve.fi/ (Curve pool yields)
- **Convex Finance:** https://www.convexfinance.com/ (Curve optimizer yields)
- **Yearn.fi:** https://yearn.fi/ (Yearn vault yields)
- **Lido:** https://stake.lido.fi/ (stETH staking APY)
- **Rocket Pool:** https://rocketpool.net/ (rETH staking APY)

### BNB Smart Chain
- **PancakeSwap:** https://pancakeswap.finance/farms (CAKE farm yields)
- **Venus Protocol:** https://venus.io/ (Lending/borrowing APYs)
- **Alpaca Finance:** https://app.alpacafinance.org/lend (Lending vault APYs)
- **Beefy BSC:** https://app.beefy.com/ (Vault yields on BSC)

### Solana
- **Marinade:** https://marinade.finance/ (mSOL staking)
- **Jito:** https://www.jito.network/ (JitoSOL staking with MEV rewards)
- **Raydium:** https://raydium.io/clmm/pools (Liquidity pool yields)
- **Orca:** https://www.orca.so/pools (Whirlpool yields)

### Arbitrum/Optimism
- **Aave V3:** https://app.aave.com/markets (Arbitrum/Optimism yields)
- **Uniswap V3:** https://app.uniswap.org/pools (L3 pool yields)
- **Velodrome:** https://app.velodrome.finance/ (Optimism yields)
- **Camelot:** https://app.camelot.exchange/ (Arbitrum yields)

### Polygon
- **QuickSwap:** https://quickswap.exchange/ (DEX yields)
- **Aave Polygon:** https://aave.com/markets (Lending on Polygon)

---

## Yield Aggregator Platforms (For Checking Vault Yields)

### Beefy Finance
**URL:** https://beefy.com/
**Chains:** 39 chains
**Coverage:** 500+ vaults

**API:**
```bash
# All vaults
GET https://api.beefy.finance/vaults

# Vaults by chain
GET https://api.beefy.finance/vaults/tvl?chain=bsc

# Single vault details
GET https://api.beefy.finance/vaults/{vault_address}
```

### Yearn Finance
**URL:** https://yearn.fi/
**Chains:** Ethereum, Arbitrum, Optimism

**API:**
```bash
# All vaults
GET https://api.yearn.fi/v1/chains/ethereum/vaults/all

# Single vault
GET https://api.yearn.fi/v1/chains/ethereum/vaults/{vault_address}
```

### Autofarm
**URL:** https://autofarm.network/
**Chains:** Multi-chain (BSC, Polygon, etc.)

### ACryptoS
**URL:** https://app.acryptos.com/
**Chains:** BSC, Cronos, Polygon, etc.

---

## Open Source Yields Trackers (GitHub)

### DefiLlama Yield Server
**Repo:** https://github.com/DefiLlama/yield-server
**Description:** Open-source APY server powering DefiLlama
**Language:** TypeScript/JavaScript
**Features:**
- Adapter-based architecture
- On-chain data fetching
- APY calculation methodology (minimum attainable yield)
- Schema for pool data (apyBase, apyReward)

**Usage:**
```bash
git clone https://github.com/DefiLlama/yield-server
cd yield-server
npm install
npm run start
# Server runs on port 3001
# GET http://localhost:3001/pools
```

### DefiLlama DefiLlama-Adapters
**Repo:** https://github.com/DefiLlama/DefiLlama-Adapters
**Description:** Adapters for computing TVL
**Language:** TypeScript
**Usage:** Learn protocol integration for custom yield tracking

### DefiLlama App
**Repo:** https://github.com/DefiLlama/defillama-app
**Description:** Main DefiLlama application code
**Language:** TypeScript
**Usage:** Build custom dashboard using DefiLlama data

### defi-yields-mcp
**Repo:** https://github.com/kukapay/defi-yields-mcp
**Description:** MCP server for AI agents to explore DeFi yields
**Language:** JavaScript
**Features:**
- `get_yield_pools` tool
- Powered by DefiLlama
- Built for AI agent integration

### defi-yield-aggregator
**Repo:** https://github.com/obinnafranklinduru/defi-yield-aggregator
**Description:** Yield aggregator smart contract example
**Language:** Solidity
**Features:**
- Dynamic allocation between Aave and Compound
- Switches based on higher APY

### yapt
**Repo:** https://github.com/yaptfi/yapt
**Description:** Stablecoin portfolio tracker with true APY
**Language:** TypeScript
**Features:**
- True APY tracking (realized, not advertised)
- Multi-protocol support (Aave, Curve, Yearn, Uniswap)

### defi-yield-dashboard
**Repo:** https://github.com/leningradtank/defi-yield-dashboard
**Description:** DeFi yield dashboard with Jupyter Notebook
**Language:** Jupyter Notebook
**Features:**
- Pulls lending/borrowing data from multiple protocols
- Analyze and visualize yields

---

## APIs for Programmatic Access

### DefiLlama API (Yields)
**Base URL:** https://yields.llama.fi/

**Endpoints:**

```bash
# Get all yield pools
curl https://yields.llama.fi/pools

# Get pools by chain
curl https://yields.llama.fi/pools?chain=ethereum

# Get pools by token
curl https://yields.llama.fi/pools?token=bnb

# Get specific pool
curl https://yields.llama.fi/chart/{pool_id}

# Get borrow rates
curl https://yields.llama.fi/borrow

# Get LSD rates
curl https://yields.llama.fi/lsdRates

# Get yields history
curl https://yields.llamaifi/chart/{pool}
```

**Python Example:**
```python
import requests

def get_defillama_yields(chain=None, token=None):
    base_url = "https://yields.llama.fi/pools"
    params = {}
    if chain:
        params['chain'] = chain
    if token:
        params['token'] = token
    response = requests.get(base_url, params=params)
    return response.json()

# Get BNB yields on BSC
bnb_yields = get_defillama_yields(chain='bsc', token='bnb')
for pool in bnb_yields['data']:
    print(f"{pool['pool']}: {pool['apy']}% APY, TVL: ${pool['tvlUsd']:,.0f}")
```

### Beefy API
**Base URL:** https://api.beefy.finance/

**Endpoints:**
```bash
# All vaults
curl https://api.beefy.finance/vaults

# Vaults by chain
curl https://api.beefy.finance/vaults/tvl?chain=bsc

# Single vault details
curl https://api.beefy.finance/vaults/{vault_address}
```

### Yearn API
**Base URL:** https://api.yearn.fi/v1/

**Endpoints:**
```bash
# All Ethereum vaults
curl https://api.yearn.fi/v1/chains/ethereum/vaults/all

# Single vault
curl https://api.yearn.fi/v1/chains/ethereum/vaults/{vault_address}
```

---

## Custom Yield Tracking Scripts

### Fetch DefiLlama Yields (Python)
```python
#!/usr/bin/env python3
import requests
import json
from datetime import datetime

def fetch_yields(chain=None, token=None, min_apy=0):
    """Fetch yields from DefiLlama"""
    url = "https://yields.llama.fi/pools"
    params = {}
    if chain:
        params['chain'] = chain
    if token:
        params['token'] = token

    response = requests.get(url, params=params)
    data = response.json()

    # Filter by min APY
    filtered_pools = [
        p for p in data['data'] if p.get('apy', 0) >= min_apy
    ]

    # Sort by APY descending
    filtered_pools.sort(key=lambda x: x.get('apy', 0), reverse=True)

    return filtered_pools

def display_pools(pools, top_n=10):
    """Display top pools"""
    print(f"\n{'Pool':<50} {'Chain':<10} {'Protocol':<15} {'APY':<10} {'TVL':<15}")
    print("=" * 100)

    for i, pool in enumerate(pools[:top_n], 1):
        pool_name = pool['pool'][:47] + '...' if len(pool['pool']) > 50 else pool['pool']
        chain = pool['chain']
        protocol = pool['project'][:12] + '...' if len(pool['project']) > 15 else pool['project']
        apy = f"{pool.get('apy', 0):.2f}%"
        tvl = f"${pool.get('tvlUsd', 0):,.0f}"

        print(f"{pool_name:<50} {chain:<10} {protocol:<15} {apy:<10} {tvl:<15}")

if __name__ == "__main__":
    # Example: Get BNB yields on BSC with >5% APY
    print(f"Fetching yields at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    pools = fetch_yields(chain='bsc', token='bnb', min_apy=5)
    display_pools(pools, top_n=20)
```

### Compare Protocols (Bash)
```bash
#!/bin/bash

# Compare BNB yields across protocols
echo "Fetching BNB yields from DefiLlama..."
curl -s "https://yields.llama.fi/pools?token=bnb" | \
  jq -r '.data[] | "\(.pool) | \(.chain) | \(.project) | \(.apy)% APY | TVL: $\(.tvlUsd)"' | \
  grep -E "(BSC|Binance)" | \
  sort -t'|' -k4 -rn | \
  head -20

echo ""
echo "--- Top 20 BNB Yields on BSC ---"
```

### Monitor Specific Pool (Node.js)
```javascript
// monitor-pool.js

async function monitorPool(poolId) {
  const response = await fetch(`https://yields.llama.fi/chart/${poolId}`);
  const data = await response.json();

  const apyHistory = data.data;
  const currentApy = apyHistory[apyHistory.length - 1].apy;
  const tvl = apyHistory[apyHistory.length - 1].tvlUsd;

  console.log(`Pool ID: ${poolId}`);
  console.log(`Current APY: ${currentApy.toFixed(2)}%`);
  console.log(`Current TVL: $${tvl.toLocaleString()}`);
  console.log(`Data points: ${apyHistory.length}`);

  // Calculate 7-day average
  const last7Days = apyHistory.slice(-7);
  const avgApy = last7Days.reduce((sum, point) => sum + point.apy, 0) / last7Days.length;
  console.log(`7-day average APY: ${avgApy.toFixed(2)}%`);
}

// Usage
monitorPool('0x1234...');  // Replace with pool ID
```

---

## Alerting and Notifications

### Set Up APY Alerts
```python
import requests
import smtplib
from email.mime.text import MIMEText

def check_apy_and_alert(pool_id, threshold_apy, email, password, to_email):
    """Check if APY dropped below threshold and send email alert"""
    url = f"https://yields.llama.fi/chart/{pool_id}"
    response = requests.get(url)
    data = response.json()

    current_apy = data.data[-1].apy

    if current_apy < threshold_apy:
        msg = MIMEText(f"Alert: APY dropped to {current_apy:.2f}% (threshold: {threshold_apy}%)")
        msg['Subject'] = 'Yield Alert'
        msg['From'] = email
        msg['To'] = to_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)
            server.send_message(msg)

        print("Alert sent!")
    else:
        print(f"APY is {current_apy:.2f}%, above threshold")
```

---

## Data Quality Tips

### Verify Data
1. **Cross-check multiple sources:** DefiLlama + protocol dashboard
2. **Check timestamps:** Ensure data is recent (last 24 hours)
3. **Verify pool addresses:** Match with official protocol docs
4. **Check TVL:** Low TVL may indicate stale or inactive pools
5. **Look for outliers:** Extremely high APYs may be temporary or risky

### Common Issues
- **Stale data:** Some aggregators don't update frequently
- **Inaccurate APY calculation:** Some show gross APY before fees
- **Pool deactivation:** Check if pool is still active
- **Incentive programs:** Short-term APY boosts may expire soon
- **Reward token price volatility:** APY can swing wildly with token price

---

## Best Practices

### For Research
1. Start with DefiLlama (most comprehensive)
2. Cross-reference with official protocol dashboards
3. Check DefiLlama "Reputation Score" for protocol risk
4. Look at 30-day mean APY (more stable than snapshot)
5. Consider TVL as proxy for safety

### For Automation
1. Use DefiLlama API (reliable, well-documented)
2. Implement retry logic for API calls
3. Cache data to avoid rate limiting
4. Set up monitoring for data anomalies
5. Log all data fetches for audit trail

### For Decision Making
1. Don't chase highest APY (often highest risk)
2. Consider sustainable yields (protocol fees) vs. token emissions
3. Factor in transaction costs (gas fees eat yield)
4. Consider lock-up periods and liquidity
5. Diversify across protocols and strategies
