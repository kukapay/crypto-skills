#!/usr/bin/env python3
"""
Fetch Yields from DefiLlama API

This script fetches yield opportunities from DefiLlama for specified chains and tokens,
filters by APY, and displays top results.

Usage:
    python fetch-defillama-yields.py --chain bsc --token bnb --min-apy 5 --top 20
    python fetch-defillama-yields.py --token eth --min-apy 3
    python fetch-defillama-yields.py --chain ethereum --top 50
"""

import requests
import argparse
import json
from datetime import datetime
from typing import List, Dict, Optional


def fetch_yields(
    chain: Optional[str] = None, token: Optional[str] = None, min_tvl: float = 0
) -> List[Dict]:
    """
    Fetch yield pools from DefiLlama API.

    Args:
        chain: Filter by blockchain (e.g., 'ethereum', 'bsc', 'arbitrum')
        token: Filter by token (e.g., 'bnb', 'eth', 'usdc')
        min_tvl: Minimum TVL in USD

    Returns:
        List of yield pool dictionaries
    """
    base_url = "https://yields.llama.fi/pools"
    params = {}
    if chain:
        params["chain"] = chain
    if token:
        params["token"] = token

    try:
        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        filtered_pools = [p for p in data["data"] if p.get("tvlUsd", 0) >= min_tvl]

        return filtered_pools

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def filter_by_apy(pools: List[Dict], min_apy: float) -> List[Dict]:
    """Filter pools by minimum APY."""
    return [p for p in pools if p.get("apy", 0) >= min_apy]


def sort_by_apy(pools: List[Dict]) -> List[Dict]:
    """Sort pools by APY in descending order."""
    return sorted(pools, key=lambda x: x.get("apy", 0), reverse=True)


def display_pools(pools: List[Dict], top_n: int = 20, show_details: bool = False):
    """
    Display yield pools in formatted table.

    Args:
        pools: List of pool dictionaries
        top_n: Number of top pools to display
        show_details: Show additional details (30-day mean, stablecoin, etc.)
    """
    if not pools:
        return

    top_pools = pools[:top_n]

    print(
        f"\n{'Pool':<50} {'Chain':<10} {'Protocol':<15} {'APY':<10} {'30d Mean':<10} {'TVL':<15}"
    )
    print("=" * 115)

    for pool in top_pools:
        pool_name = (
            pool["pool"][:47] + "..." if len(pool["pool"]) > 50 else pool["pool"]
        )
        chain = pool["chain"]
        protocol = (
            pool["project"][:12] + "..."
            if len(pool["project"]) > 15
            else pool["project"]
        )
        apy = f"{pool.get('apy', 0):.2f}%" if pool.get("apy") else "N/A"
        apy_mean30d = (
            f"{pool.get('apyMean30d', 0):.2f}%" if pool.get("apyMean30d") else "N/A"
        )
        tvl = f"${pool.get('tvlUsd', 0):,.0f}"

        print(
            f"{pool_name:<50} {chain:<10} {protocol:<15} {apy:<10} {apy_mean30d:<10} {tvl:<15}"
        )

        if show_details:
            print(
                f"  Symbol: {pool.get('symbol', 'N/A')} | "
                f"Stablecoin: {pool.get('stablecoin', False)} | "
                f"Base APY: {pool.get('apyBase', 0):.2f}% | "
                f"Reward APY: {pool.get('apyReward', 0):.2f}%"
            )

    print(f"\nShowing {len(top_pools)} of {len(pools)} total pools")


def get_summary_stats(pools: List[Dict]) -> Dict:
    """Get summary statistics for the pools."""
    if not pools:
        return {}

    apys = [p.get("apy", 0) for p in pools if p.get("apy")]
    tvls = [p.get("tvlUsd", 0) for p in pools if p.get("tvlUsd")]

    return {
        "total_pools": len(pools),
        "avg_apy": sum(apys) / len(apys) if apys else 0,
        "max_apy": max(apys) if apys else 0,
        "min_apy": min(apys) if apys else 0,
        "total_tvl": sum(tvls),
        "median_apy": sorted(apys)[len(apys) // 2] if apys else 0,
    }


def export_to_json(pools: List[Dict], filename: str):
    """Export pools to JSON file."""
    with open(filename, "w") as f:
        json.dump(pools, f, indent=2)
    print(f"\nExported {len(pools)} pools to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and display DeFi yields from DefiLlama"
    )
    parser.add_argument(
        "--chain", "-c", help="Filter by blockchain (e.g., ethereum, bsc, arbitrum)"
    )
    parser.add_argument("--token", "-t", help="Filter by token (e.g., bnb, eth, usdc)")
    parser.add_argument(
        "--min-apy",
        "-a",
        type=float,
        default=0,
        help="Minimum APY threshold (default: 0)",
    )
    parser.add_argument(
        "--min-tvl", type=float, default=0, help="Minimum TVL in USD (default: 0)"
    )
    parser.add_argument(
        "--top",
        "-n",
        type=int,
        default=20,
        help="Number of top pools to display (default: 20)",
    )
    parser.add_argument("--export", "-e", help="Export results to JSON file")
    parser.add_argument(
        "--details", "-d", action="store_true", help="Show additional pool details"
    )
    parser.add_argument(
        "--json-only", action="store_true", help="Only export JSON, no table output"
    )

    args = parser.parse_args()

    print(
        f"Fetching yields from DefiLlama at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    filters = []
    if args.chain:
        filters.append(f"chain={args.chain}")
    if args.token:
        filters.append(f"token={args.token}")
    if args.min_apy > 0:
        filters.append(f"min_apy={args.min_apy}%")
    if args.min_tvl > 0:
        filters.append(f"min_tvl=${args.min_tvl:,.0f}")

    if filters:
        print(f"Filters: {', '.join(filters)}")

    pools = fetch_yields(chain=args.chain, token=args.token, min_tvl=args.min_tvl)

    if not pools:
        print("No pools found.")
        return

    # Filter by APY
    if args.min_apy > 0:
        pools = filter_by_apy(pools, args.min_apy)

    if not pools:
        print(f"No pools found with APY >= {args.min_apy}%.")
        return

    pools = sort_by_apy(pools)

    stats = get_summary_stats(pools)
    print(f"\nSummary:")
    print(f"  Total pools: {stats['total_pools']}")
    print(f"  Average APY: {stats['avg_apy']:.2f}%")
    print(f"  Median APY: {stats['median_apy']:.2f}%")
    print(f"  Max APY: {stats['max_apy']:.2f}%")
    print(f"  Total TVL: ${stats['total_tvl']:,.0f}")

    if not args.json_only:
        display_pools(pools, top_n=args.top, show_details=args.details)

    if args.export:
        export_to_json(pools, args.export)


if __name__ == "__main__":
    main()
