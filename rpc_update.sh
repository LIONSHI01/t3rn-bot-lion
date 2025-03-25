#!/bin/bash

read -p "Base Sepolia RPC: " BASE_SEPOLIA_RPC
if [ -z "$BASE_SEPOLIA_RPC" ]; then
    echo "Error: RPC URL cannot be empty"
    exit 1
fi
if grep -q "^BASE_SEPOLIA_RPC=" .env; then
    sed -i.bak "s|^BASE_SEPOLIA_RPC=.*|BASE_SEPOLIA_RPC=${BASE_SEPOLIA_RPC}|" .env
    echo "Updated BASE_SEPOLIA_RPC to ${BASE_SEPOLIA_RPC}"
else
    echo "BASE_SEPOLIA_RPC=${BASE_SEPOLIA_RPC}" >> .env
    echo "Added BASE_SEPOLIA_RPC as ${BASE_SEPOLIA_RPC}"
fi

read -p "OP Sepolia RPC: " OP_SEPOLIA_RPC
if [ -z "$OP_SEPOLIA_RPC" ]; then
    echo "Error: RPC URL cannot be empty"
    exit 1
fi
if grep -q "^OP_SEPOLIA_RPC=" .env; then
    sed -i.bak "s|^OP_SEPOLIA_RPC=.*|OP_SEPOLIA_RPC=${OP_SEPOLIA_RPC}|" .env
    echo "Updated OP_SEPOLIA_RPC to ${OP_SEPOLIA_RPC}"
else
    echo "OP_SEPOLIA_RPC=${OP_SEPOLIA_RPC}" >> .env
    echo "Added OP_SEPOLIA_RPC as ${OP_SEPOLIA_RPC}"
fi