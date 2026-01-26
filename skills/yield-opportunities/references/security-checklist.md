# Protocol Security Checklist

Use this checklist to vet DeFi protocols before recommending or using them.

## Phase 1: Basic Vetting (Do This First)

### Documentation & Transparency
- [ ] **Official website exists and is professional**
- [ ] **Clear documentation site** (docs.*, not just Medium posts)
- [ ] **Smart contract addresses publicly disclosed** on official site
- [ ] **Tokenomics page** exists (if Protocol has token)
- [ ] **Team section** with profiles (even if pseudonymous)
- [ ] **Social media presence** (Twitter, Discord, Telegram)
- [ ] **Activity level:** Recent posts/announcements (last 30 days)

### Contract Verification
- [ ] **Contracts verified on block explorer** (Etherscan, BscScan, etc.)
- [ ] **Source code is open-source** and readable
- [ ] **Proxy contract pattern used properly** (upgradeability transparent)
- [ ] **Implementation contract** accessible

## Phase 2: Security Audits

### Audit Presence
- [ ] **At least one audit** from reputable firm
- [ ] **Recent audit** (within last 12-18 months)
- [ ] **Audit reports publicly available** (PDF on website)
- [ ] **Findings addressed publicly** (issues fixed/mitigated)

### Reputable Audit Firms (In Order of Preference)

**Tier 1 (Best):**
- OpenZeppelin
- ConsenSys Diligence
- Trail of Bits
- Certik
- Quantstamp
- Sigma Prime
- PeckShield

**Tier 2 (Good but lower):**
- SlowMist
- Haechi Labs
- MixBytes
- Paladin Blockchain Security
- Armors

**Tier 3 (Questionable):**
- Unknown or very small firms
- Self-audits
- "Audit in progress" for months

### Audit Review Checklist
- [ ] **Critical findings:** Were any? Fixed?
- [ ] **High findings:** Were any? Addressed?
- [ ] **Medium findings:** Addressed or acknowledged?
- [ ] **Low findings:** Minor issues?
- [ ] **Total findings:** <10 is ideal, 10-25 common, >25 concerning

## Phase 3: Track Record & Battle Testing

### TVL and Age
- [ ] **Total Value Locked (TVL)** on DefiLlama
  - >$500M: Excellent, highly battle-tested
  - $100-500M: Good, moderate track record
  - $10-100M: New, emerging
  - <$10M: Experimental, high diligence required
- [ ] **Protocol age:** How long has it been deployed?
  - >2 years: Very mature
  - 1-2 years: Mature
  - 6-12 months: New
  - <6 months: Very new, caution

### Incident History
- [ ] **No major hacks or exploits**
- [ ] **No critical incidents** on Rekt.news or similar
- [ ] **Past issues** handled transparently with post-mortems
- [ ] **Response to incidents:** Quick, appropriate compensation if applicable

### Community Sentiment
- [ ] **Active Discord/Telegram** with real users
- [ ] **Moderators respond** to questions and issues
- [ ] **No major FUD campaigns** without addressing
- [ ] **Respected in crypto community** (not on scam lists)

## Phase 4: Technical Deep Dive

### Code Quality
- [ ] **Clean, readable code** (not obfuscated)
- [ ] **Follows industry standards** (ERC-20, ERC-4626, etc.)
- [ ] **Uses battle-tested libraries** (OpenZeppelin, etc.)
- [ ] **Not overly complex** (simpler is often safer)
- [ ] **No suspicious patterns** (hidden fees, backdoors, etc.)

### Upgradeability
- [ ] **Proxy pattern transparent** (UUPS, Transparent, Beacon)
- [ ] **Upgrade delay** (timelocks implemented)
- [ ] **Governance for upgrades** (not admin keys)
- [ ] **Past upgrades documented** and explained

### Permission Controls
- [ ] **Admin role:** Limited permissions, ideally only upgrades
- [ ] **Timelocks:** In place for privileged operations
- [ ] **Multi-sig used** for critical operations (preferably >2 signers)
- [ ] **Team wallet addresses** trackable on-chain

## Phase 5: Token & Governance

### Token Economics (if applicable)
- [ ] **Vesting schedule clear** and reasonable
- [ ] **Team not dumping** tokens (check recent transfers)
- [ ] **Circulating vs. Total supply** disclosed
- [ ] **Inflation schedule** sustainable
- [ ] **Token has utility** (governance, rewards, etc.)

### Governance
- [ ] **DAO governance active** (or clear reason why not)
- [ ] **Governance proposals** visible and discussed
- [ ] **Voting power decentralized** (not just insiders)
- [ ] **Treasury management** transparent

## Phase 6: Red Flags (Immediate Disqualification)

### Critical Red Flags (Don't Use)
- [ ] **No audit** or extremely old audit (>2 years)
- [ ] **Contracts not verified** on block explorer
- [ ] **Anonymous owner** + no community presence
- [ ] **Team tokens dumped** recently (check Etherscan/BscScan)
- [ ] **Obfuscated code** or code hidden behind proxy only
- [ ] **Unlimited minting** function accessible to admin
- [ ] **Unlimited withdraw/steal** function accessible to admin
- [ ] **Backdoor** or hidden code patterns
- [ ] **Promises unrealistic APY** (>1000% not sustainable)
- [ ] **Pump and dump patterns** (high initial APY, then crash)
- [ ] **Copy-paste** of known exploited contracts
- [ ] **Team involved in** previous scams/exploits
- [ ] **No contact/support** channel
- [ ] **Pressure to deposit quickly** (FOMO tactics)

### Warning Signs (Proceed with Caution)
- [ ] **TVL fluctuating wildly** (possible manipulation)
- [ ] **Anonymous team** but good community/support
- [ ] **New audit** from unknown firm
- [ ] **Governance inactive** or controlled by insiders
- [ ] **Token heavily manipulated** on DEX
- [ ] **Social media** full of shilling vs. real discussion
- [ ] **Aggressive marketing** vs. substance
- [ ] **Paying influencers** (some may be legitimate, some not)

## Phase 7: Operational Security

### Oracle Usage
- [ ] **Oracles secure and decentralized** (Chainlink, Band)
- [ ] **Not using single-source** price feeds that can be manipulated
- [ ] **Flash loan protection** implemented

### Reentrancy Protection
- [ ] **Reentrancy guards** on critical functions
- [ ] **Checks-Effects-Interactions** pattern followed
- [ ] **No external calls** in critical state changes

### Integer Overflow/Underflow
- [ ] **Solidity 0.8+** used (handles overflow/underflow automatically)
- [ ] **SafeMath** used if Solidity <0.8

### Emergency Functionality
- [ ] **Emergency pause** function exists
- [ ] **Emergency withdraw** function exists (in case of bugs)
- [ ] **Pause mechanism** not easily abused

## Scoring System

### Score Calculation

| Category | Points Possible |
|----------|-----------------|
| Documentation | 0-10 |
| Audits | 0-15 |
| Track Record | 0-15 |
| Technical Quality | 0-20 |
| Token/Governance | 0-15 |
| Operational Security | 0-15 |
| Red Flags (subtraction) | -0 to -50 |

**Total Possible Score: 0-90** (Red flags can push negative)

### Score Interpretation

| Score Range | Rating | Recommendation |
|-------------|--------|----------------|
| 70-90 | Excellent | Safe to use, recommend |
| 50-69 | Good | Generally safe, use with normal precautions |
| 30-49 | Moderate | Use smaller amounts, due diligence required |
| 10-29 | Poor | High risk, avoid unless comfortable with risk |
| 0-9 or below | Very Poor | Do not use, likely scam |

## Quick Vetting Workflow (5 minutes)

### Step 1 (1 min): Basic Check
- Visit official website
- Check docs exist
- Find contract address on block explorer
- Check for audit badge/link

**Fail if:** No docs, no audit, contracts not verified

### Step 2 (2 min): Security & Track Record
- Open audit PDF, check critical findings
- Check DefiLlama for TVL and age
- Google "[Protocol] hack" or "[Protocol] exploit"
- Check Twitter/Discord for activity

**Fail if:** Critical audit findings unfixed, >$10M hack history, inactive community

### Step 3 (2 min): Red Flags & Tokenomics
- Scan smart contracts for suspicious functions (mint, withdraw)
- Check recent team token transfers (on explorer)
- Check token chart for pump-dump patterns
- Verify team doxxing or at least community trust

**Fail if:** Unlimited mint to admin, team dumping, obvious pump-dump

## Example Vetting

### Example 1: Lido Finance (Should Pass)

**Documentation:** ✅ Professional, extensive docs
**Audits:** ✅ OpenZeppelin, ConsenSys, multiple others
**Track Record:** ✅ $10B+ TVL, 2+ years, no major hacks
**Technical:** ✅ Solidity 0.8+, battle-tested, standard patterns
**Token:** ✅ LDO has governance, reasonable vesting
**Security:** ✅ Chainlink oracles, reentrancy guards, pause functions

**Score:** ~85/90 - **Excellent**

### Example 2: New Yield Farm Ape (Should Fail)

**Documentation:** ❌ Only Medium posts, no docs site
**Audits:** ❌ No audit or audit in progress for months
**Track Record:** ❌ Deployed 2 days ago, $50k TVL
**Technical:** ❌ Contracts not verified, can't review
**Token:** ❌ Anonymous team, 95% of supply to team
**Security:** ❌ Can't assess (contracts not verified)

**Score:** ~-20/90 - **Do Not Use**

## References

### Tools for Vetting
- **DefiLlama:** https://defillama.com/ (TVL, age, protocol data)
- **Etherscan/BscScan:** https://etherscan.io/ (contract verification, code)
- **Rekt.news:** https://rekt.news/ (exploit history)
- **Token Unlocks:** https://token.unlocks.app/ (vesting schedules)
- **Open Source:** https://github.com/ (code review if repo exists)

### Audit Repositories
- **OpenZeppelin:** https://blog.openzeppelin.com/
- **ConsenSys Diligence:** https://diligence.consensys.net/audits/
- **Certik:** https://www.certik.com/projects/
- **Quantstamp:** https://www.quantstamp.com/audits

### Community Resources
- **Crypto Twitter:** Search for protocol name + sentiment
- **Discord/Telegram:** Join, read discussions, ask questions
- **Twitter Lists:** Follow reputable DeFi researchers
- **Governance Forums:** Read recent proposals and discussions
