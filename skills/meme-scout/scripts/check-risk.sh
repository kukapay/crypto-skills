#!/bin/bash

# Basic risk check script for meme coins
# Usage: ./check-risk.sh <token_address> <chain>

TOKEN=$1
CHAIN=$2

if [ -z "$TOKEN" ] || [ -z "$CHAIN" ]; then
  echo "Usage: $0 <token_address> <chain>"
  echo "Example: $0 EqbJLmrcip2T9ULueB1Lj4ew4YzUs9WatGWfh5opump solana"
  exit 1
fi

echo "Risk Check for Token: $TOKEN on $CHAIN"
echo "======================================"

if [ "$CHAIN" = "solana" ]; then
  echo "RugCheck.xyz: https://rugcheck.xyz/tokens/$TOKEN"
  echo "Solana Tracker: https://www.solanatracker.io/token/$TOKEN"
fi

echo "DexScreener: Search for the token to find pair page"
echo "General checks:"
echo "- Creator wallet analysis"
echo "- Liquidity lock status"
echo "- Token distribution"
echo "- Social media presence"
echo ""
echo "WARNING: Always DYOR. Meme coins are high risk."