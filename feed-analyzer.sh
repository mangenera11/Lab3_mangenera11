#!/bin/bash

FILE="twitter_dataset.csv"

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

echo "=== TOP 5 MOST ACTIVE USERS ==="
tr -d '\r' < "$FILE" | cut -d',' -f2 | grep -v "^Username$" | sort | uniq -c | sort -nr | head -n 5
