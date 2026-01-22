# DexScreener API Reference

DexScreener provides trending data via embedded JSON in their web pages.

## Trending Endpoints

The trending data is available by fetching the HTML and extracting window.__SERVER_DATA.

### Timeframes

- 5m: ?rankBy=trendingScoreM5&order=desc
- 1h: ?rankBy=trendingScoreH1&order=desc
- 6h: (default)
- 24h: ?rankBy=trendingScoreH24&order=desc

### Data Structure

The pairs array contains objects with:

- chainId: string (e.g., "solana")
- dexId: string (e.g., "pumpswap")
- baseToken: {name, symbol, address}
- quoteToken: {name, symbol, address}
- price: string
- priceUsd: string
- priceChange: {m5, h1, h6, h24} percentages
- volume: {m5, h1, h6, h24}
- liquidity: {usd, base, quote}
- marketCap, fdv
- pairAddress
- pairCreatedAt

## Official API

DexScreener has an official API at https://docs.dexscreener.com/api/reference

But trending is not directly available; use the embedded data method.</content>
<parameter name="filePath">./skills/meme-scout/references/dexscreener-api.md