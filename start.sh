#!/bin/bash

# Natro Macro for macOS
# Copyright © Natro Team

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${CYAN}Starting Natro Macro for macOS...${NC}"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}Error: Python $REQUIRED_VERSION or higher is required. You have Python $PYTHON_VERSION.${NC}"
    exit 1
fi

# Install dependencies if needed
echo -e "${BLUE}Checking dependencies...${NC}"
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

source venv/bin/activate

echo -e "${YELLOW}Installing/updating dependencies...${NC}"
pip install -r requirements.txt

# Check if Roblox is running
if ! pgrep -f "RobloxPlayer" > /dev/null; then
    echo -e "${RED}Warning: Roblox does not appear to be running.${NC}"
    echo -e "${YELLOW}Please start Roblox and Bee Swarm Simulator before running the macro.${NC}"
    read -p "Press Enter to continue anyway..."
fi

# Delay if specified
if [ ! -z "$1" ]; then
    DELAY=$1
    echo -e "${GREEN}Starting Natro Macro in $DELAY seconds...${NC}"
    echo -e "${GREEN}Press Ctrl+C to cancel.${NC}"
    sleep $DELAY
fi

# Start the main script
echo -e "${GREEN}Starting Natro Macro...${NC}"
python3 natro_macro.py "$@"

deactivate
