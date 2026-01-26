#!/bin/bash
# Compare Yields Across Protocols
# This script fetches yield data from DefiLlama and compares protocols for a specific token

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Compare DeFi yields across protocols for a specific token.

OPTIONS:
    -t, --token TOKEN       Token to compare (e.g., bnb, eth, usdc) [required]
    -c, --chain CHAIN       Chain to filter by (e.g., bsc, ethereum, arbitrum) [optional]
    -m, --min-apy APY       Minimum APY threshold (default: 0) [optional]
    -n, --top N             Number of top protocols to display (default: 10) [optional]
    -e, --export FILE       Export results to CSV file [optional]
    -h, --help              Show this help message

EXAMPLES:
    # Compare BNB yields on BSC
    $0 --token bnb --chain bsc

    # Compare ETH yields, top 20, >5% APY
    $0 --token eth --min-apy 5 --top 20

    # Compare stablecoin yields, export to CSV
    $0 --token usdc --min-apy 3 --export stablecoin-yields.csv

EOF
}

TOKEN=""
CHAIN=""
MIN_APY=0
TOP_N=10
EXPORT_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--token)
            TOKEN="$2"
            shift 2
            ;;
        -c|--chain)
            CHAIN="$2"
            shift 2
            ;;
        -m|--min-apy)
            MIN_APY="$2"
            shift 2
            ;;
        -n|--top)
            TOP_N="$2"
            shift 2
            ;;
        -e|--export)
            EXPORT_FILE="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
    exit 1
    ;;
    esac
done

if [[ -z "$TOKEN" ]]; then
    echo -e "${RED}Error: TOKEN is required${NC}"
    usage
    exit 1
fi

URL="https://yields.llama.fi/pools?token=${TOKEN^^}"

if [[ -n "$CHAIN" ]]; then
    URL="${URL}&chain=${CHAIN}"
fi

echo -e "${BLUE}Fetching yields from DefiLlama...${NC}"
echo "Token: ${TOKEN^^}"
if [[ -n "$CHAIN" ]]; then
    echo "Chain: $CHAIN"
fi
echo "Min APY: $MIN_APY%"
echo ""

DATA=$(curl -s "$URL")

if [[ $? -ne 0 ]]; then
    echo -e "${RED}Error: Failed to fetch data from DefiLlama${NC}"
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo -e "${RED}Error: jq is required but not installed${NC}"
    echo "Install jq: sudo apt-get install jq (Ubuntu/Debian) or brew install jq (macOS)"
    exit 1
fi

PROTOCOLS=$(echo "$DATA" | \
    jq -r ".data[] | select(.apy >= $MIN_APY) | \"\(.project)|\(.pool)|\(.chain)|\(.apy)|\(.tvlUsd)|\(.stablecoin)\"" | \
    sort -t'|' -k4 -rn | \
    head -n "$TOP_N" \
)

if [[ -z "$PROTOCOLS" ]]; then
    echo -e "${YELLOW}No protocols found matching criteria${NC}"
    exit 0
fi

printf "\n${GREEN}%-20s %-40s %-10s %-12s %-15s %-10s${NC}\n" \
    "Protocol" "Pool" "Chain" "APY" "TVL" "Stable?"
printf "${GREEN}%-20s %-40s %-10s %-12s %-15s %-10s${NC}\n" \
    "--------" "----" "-----" "---" "---" "------"

CSV_DATA="Protocol,Pool,Chain,APY,TVL,Stablecoin,count"
PROTOCOL_COUNT=1

while IFS='|' read -r protocol pool chain apy tvl stable; do
    tvl_formatted=$(printf "%'d" $(echo "$tvl" | cut -d'.' -f1))
    apy_formatted=$(printf "%.2f%%" "$apy")

    if [[ "$stable" == "true" ]]; then
        stable_formatted="${GREEN}Yes${NC}"
    else
        stable_formatted="${YELLOW}No${NC}"
    fi

    pool_display="${pool:0:35}"
    if (( ${#pool} > 35 )); then
        pool_display="${pool_display}..."
    fi

    printf "%-20s %-40s %-10s %-12s $%-14s %-10s\n" \
        "$protocol" "$pool_display" "$chain" "$apy_formatted" "$tvl_formatted" "$stable_formatted"

    CSV_DATA="${CSV_DATA}\n${protocol},${pool},${chain},${apy_formatted},$${tvl_formatted},${stable}"

    PROTOCOL_COUNT=$((PROTOCOL_COUNT + 1))
done <<< "$PROTOCOLS"

echo ""
echo -e "${BLUE}Showing $((PROTOCOL_COUNT - 1)) protocols${NC}"

if [[ -n "$EXPORT_FILE" ]]; then
    echo -e "\n${BLUE}Exporting to ${EXPORT_FILE}...${NC}"
    echo -e "$CSV_DATA" > "$EXPORT_FILE"
    echo -e "${GREEN}Export complete!${NC}"
fi

echo ""
echo -e "${BLUE}Statistics:${NC}"

TOTAL_APY=$(echo "$DATA" | jq -r "[.data[] | select(.apy >= $MIN_APY) | .apy] | add")
TOTAL_COUNT=$(echo "$DATA" | jq -r "[.data[] | select(.apy >= $MIN_APY)] | length")

if [[ -n "$TOTAL_APY" ]] && [[ -n "$TOTAL_COUNT" ]] && [[ "$TOTAL_COUNT" -gt 0 ]]; then
    AVG_APY=$(awk "BEGIN {printf \"%.2f\", ${TOTAL_APY}/${TOTAL_COUNT}}")
    echo "Average APY: ${AVG_APY}%"
    echo "Total protocols found: $((PROTOCOL_COUNT - 1))"
else
    echo "No statistics available"
fi

echo ""
echo -e "${GREEN}Done!${NC}"
