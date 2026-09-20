#!/bin/bash

# Check if an IP address was provided as an argument
if [ -z "$1" ]; then
    echo "Error: No IP address provided."
    echo "Usage: sudo ./block_ip.sh <IP_ADDRESS>"
    exit 1
fi

TARGET_IP=$1

echo "Starting containment procedure for IP: $TARGET_IP"

# Use Uncomplicated Firewall (UFW) to deny incoming traffic from the target IP
ufw deny from $TARGET_IP to any

# Reload the firewall to ensure the rule takes effect immediately
ufw reload

echo "[SUCCESS] Traffic from $TARGET_IP has been blocked."