#!/bin/bash

#Change default shell text colors:
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Involk color change with -e

LOG_PATH="/home/$(whoami)/logs/recorded_session.log"
echo -e "${GREEN}====================================================================${NC}"

echo -e "Now logging session at $LOG_PATH"

echo -e "${ORANGE}-------------------------------------------------------------------${NC}" > "$LOG_PATH"
echo -e "${ORANGE}-------------------------------------------------------------------${NC}" >> "$LOG_PATH"

# Record event and flush (f) the output to .log
# -a for append instead of reseting .log
script -a -f "$LOG_PATH"

# Use Regular expression to stop (subsitue with nothing) command like 'clear' from clearing .log content
sed -i 's/\x1b\[[0-9;]*[HJK]//g' "$LOG_PATH"

echo -e "${ORANGE}-------------------------------------------------------------------${NC}" >> "$LOG_PATH"
echo -e "${ORANGE}-------------------------------------------------------------------${NC}" >> "$LOG_PATH"

echo -e "Logging finished"
echo -e "${GREEN}====================================================================${NC}"
