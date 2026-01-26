# Risk Assessment Framework for DeFi Yield

This guide provides comprehensive risk assessment criteria for evaluating DeFi yield opportunities.

## Risk Categories

### 1. Smart Contract Risk

**Assessment Criteria:**
- **Audit Status:** Is the protocol audited? By whom? When?
  - Top auditors: OpenZeppelin, ConsenSys Diligence, Certik, Trail of Bits
  - Recent audits (last 12 months) preferred
- **Code Complexity:** Simple contracts vs. complex vaults/strategies
- **Bug History:** Has the protocol had exploits? How were they handled?
- **TVL as Proxy:** Higher TVL = more battle-tested
  - >$100M: Battle-tested, lower risk
  - $10-100M: Moderate risk
  - <$10M: Higher risk (due diligence required)

**Risk Levels:**
- **Low:** Multiple audits, $500M+ TVL, no major exploits
- **Medium:** Single audit, $50-500M TVL, minor bug fixes
- **High:** No audit or old audit, <$50M TVL
- **Extreme:** Unaudited, <24h old, anonymous team

### 2. Impermanent Loss (IL) Risk

**Understanding IL:**
- IL occurs when LP token values diverge from simply holding assets
- Formula: IL = (Current Pool Value) / (Held Value) - 1

**Risk by Pool Type:**

| Pool Type | Typical IL | Example Pair | Typical APY |
|-----------|------------|--------------|-------------|
| **Stable-Stable** | Minimal (0-2%) | USDC/USDT, DAI/USDC | 3-10% |
| **Stable-Tier 1** | Low (2-10%) | USDC/ETH, USDT/BTC | 5-20% |
| **Token-Tier 1** | Medium (10-30%) | ETH/BTC, SOL/USDC | 10-50% |
| **Token-Token** | High (30-100%+) | ALT1/ALT2, new tokens | 20-100%+ |
| **V3 Concentrated** | Very High | Any V3 range | Variable |

**Mitigation:**
- Prefer stablecoin pairs for risk-averse users
- Use single-token vaults (Beefy, ACryptoS) to avoid IL completely
- Set wider price ranges in V3 (reduces IL, reduces yield)

### 3. Price Risk (Asset Volatility)

**Key Points:**
- All yields are denominated in the native asset
- If the asset drops 50%, your USD value drops 50% regardless of APY earned
- High APY often compensates for high price volatility

**Assessment Questions:**
- Is the asset volatile (altcoins, meme tokens)?
- Is the asset stable (ETH, BTC, stables)?
- Is yield strategy dependent on price staying in range (V3)?
- Can you handle drawdown in the underlying asset?

**Mitigation:**
- Prefer stablecoins for risk-averse yield
- Hedge with futures/options if experienced
- Consider if you want long-term exposure to the asset

### 4. Liquidation Risk (Lending/Borrowing)

**When Applicable:**
- Using assets as collateral to borrow
- Leverage farming (borrow to farm)

**Risk Factors:**
- **Loan-to-Value (LTV) ratio:** How much borrowed vs. collateral
  - Safe: <50% LTV
  - Moderate: 50-70% LTV
  - Risky: >70% LTV
- **Collateral Factor:** Maximum borrow % of collateral value
- **Asset Correlation:** If collateral and borrowed asset move together

**Liquidation Threshold:**
```
If LTV = 70% and asset drops 30%, you get liquidated
If LTV = 40% and asset drops 60%, you get liquidated
```

**Mitigation:**
- Keep LTV <50% for safety
- Monitor collateral value regularly
- Use safe collateral (ETH, BTC) when borrowing volatile assets

### 5. Protocol Governance/Regulatory Risk

**Assessment Criteria:**
- **Team Anonymity:** Anonymous vs. doxxed team
- **DAO Governance:** Token voting vs. centralized control
- **Regulatory Scrutiny:** Is protocol operating in gray area?
- **Upgrade Path:** Can protocol changes be forced?
- **Revenue Model:** Does protocol have sustainable revenue?

**Risk Levels:**
- **Low:** Doxxed team, active governance, clear revenue model
- **Medium:** Pseudonymous team, early-stage governance
- **High:** Anonymous team, no governance, unaudited
- **Extreme:** Newly deployed, no track record, suspicious

### 6. Bridge Risk (Cross-Chain)

**When Applicable:**
- Bridging assets to other chains for yield

**Key Considerations:**
- **Bridge Type:** Official bridge vs. third-party
  - Official: Best (Chain-native bridge, LayerZero)
  - Established: Second best (Multichain, Celer)
  - New/Unverified: Avoid
- **Bridge Track Record:** Has it been hacked?
- ** Liquidity:** Can you bridge back easily?
- **Cost:** Bridge fees + gas costs
- **Is It Worth It?** Yield differential >5-10% to justify risk/cost

**Historical Bridge Hacks:**
- Ronin Bridge: $622M
- Wormhole: $326M
- Horizon Bridge: $100M

**Mitigation:**
- Use official bridges (BNB Chain Bridge, Arbitrum Bridge)
- Only bridge if yield significantly higher
- Keep bridged amounts small relative to portfolio
- Verify bridge is currently operational (some paused)

### 7. Token Incentive Risk

**Understanding Token Rewards:**
- Many high APYs come from emissions of protocol reward tokens
- These tokens often have poor fundamentals and dump on markets
- High emissions = high risk of token devaluation

**Assessment:**
- **Emission Rate:** How many tokens minted per day?
- **Token Distribution:** Is distribution fair or whale-heavy?
- **Token Utility:** Does token have real governance/utility or just rewards?
- **Price Trend:** Is token devaluing rapidly?

**Risk Levels:**
- **Low:** Mature protocols (AAVE, CRV), stable emissions
- **Medium:** Established protocols, moderate emissions
- **High:** New protocols, high emissions to bootstrap
- **Extreme:** Anonymous, massive emissions, obvious dumping patterns

### 8. Concentration Risk

**Definition:** Putting too much capital in one protocol or strategy

**Safe Allocations:**
- **Conservative:** No position >10% of portfolio
- **Balanced:** No position >25% of portfolio
- **Aggressive:** Can concentrate for higher yield (but acknowledge risk)

**Mitigation:**
- Diversify across protocols
- Diversify across chains
- Mix of staking, lending, LP (different risk profiles)
- Keep some in "risk-free" yield (native staking, CeFi vaults)

## Composite Risk Scoring

When evaluating a specific yield opportunity, score each category 1-5:

| Category | Score (1-5) | Weight |
|----------|-------------|--------|
| Smart Contract Risk | 1=Safe, 5=Unsafe | 25% |
| Impermanent Loss Risk | 1=Minimal, 5 Extreme | 20% |
| Price Risk | 1=Stable, 5=Volatile | 20% |
| Liquidation Risk | 1=None, 5=High | 10% |
| Protocol Risk | 1=Mature, 5=New/Unvetted | 15% |
| Bridge Risk (if bridging) | 1=None, 5=Unsafe | 0-10% |

**Overall Risk Score = Sum(Score × Weight)**

**Score Interpretation:**
- **1.0-1.5:** Very Low Risk
- **1.6-2.0:** Low Risk
- **2.1-2.5:** Medium Risk
- **2.6-3.5:** High Risk
- **3.6+ : Very High Risk**

## Risk Tolerance Profiles

### Conservative Profile
**Max Risk Score:** 2.0
**Preferred Strategies:**
- Native staking / liquid staking
- Lending (single asset)
- Stablecoin-stablecoin LP
- Single-token vaults (no IL)
- CeFi vaults (Binance Earn, etc.)

### Balanced Profile
**Max Risk Score:** 2.5
**Preferred Strategies:**
- Mix of staking + lending + stable LP
- Tier 1 asset LP (ETH/USDC, BTC/USDC)
- Yield aggregators (Beefy, Yearn)
- Small allocation to higher-yield farms

### Aggressive Profile
**Max Risk Score:** 3.5
**Preferred Strategies:**
- Token-token LP (higher yield, higher IL)
- V3 concentrated positions
- New protocol incentives
- Leverage farming (borrow to farm)
- Higher allocation to volatile assets

## Due Diligence Checklist

Before deploying to any yield strategy:

### Essential (Mandatory)
- [ ] Protocol has at least one audit from a recognized auditor
- [ ] TVL >$10M (higher is better)
- [ ] Documentation exists and is clear
- [ ] Contract addresses verified on block explorer
- [ ] Understand how yield is generated (fees, emissions, etc.)
- [ ] Understand fees and lock-up periods

### Important (Should Do)
- [ ] Check protocol's social media and Discord for activity
- [ ] Read recent governance proposals/updates
- [ ] Check for any past exploits or incidents
- [ ] Verify team (doxxed or at least known in community)
- [ ] Test with small amount first
- [ ] Understand withdrawal process and fees

### Nice to Have
- [ ] Read contract code (if technically inclined)
- [ ] Check on-chain data (utilization, TVL history)
- [ ] Monitor for whale movements
- [ ] Set up alerts for protocol news
- [ ] Community sentiment check

## Example Assessments

### Example 1: Lido Staking (stETH)

| Category | Score | Reason |
|----------|-------|--------|
| Smart Contract | 1 | Multi-audited, $10B+ TVL |
| Impermanent Loss | 1 | No IL (single asset) |
| Price Risk | 2 | ETH exposure (moderately volatile) |
| Liquidation | 1 | No borrowing involved |
| Protocol | 1 | Market leader, mature |
| Bridge | 1 | No bridging (native) |

**Overall:** 1.15 - **Very Low Risk**

### Example 2: PancakeSwap USDT-BNB LP

| Category | Score | Reason |
|----------|-------|--------|
| Smart Contract | 2 | Audited, battle-tested, but large attack surface |
| Impermanent Loss | 2 | Medium IL (stablecoin + volatile) |
| Price Risk | 3 | BNB volatility exposure |
| Liquidation | 1 | No borrowing involved |
| Protocol | 2 | Mature, largest BSC DEX |
| Bridge | 1 | Native to BSC |

**Overall:** 2.05 - **Low-Medium Risk**

### Example 3: New Protocol Farm (Random Alt-Alt LP)

| Category | Score | Reason |
|----------|-------|--------|
| Smart Contract | 4 | No audit, $1M TVL, new deployment |
| Impermanent Loss | 4 | High IL (alt-alt pair) |
| Price Risk | 5 | Highly volatile altcoins |
| Liquidation | 2 | Possible if using leverage |
| Protocol | 5 | Anonymous team, 2 days old |
| Bridge | 1 | Native (or 4 if bridged) |

**Overall:** 3.65+ - **Very High Risk - Avoid or Ape with Caution**
