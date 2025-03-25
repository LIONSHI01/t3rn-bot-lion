#!/bin/bash

read -p "Base Sepolia RPC:" BASE_SEPOLIA_RPC
read -p "OP Sepolia RPC:" OP_SEPOLIA_RPC

sed -i "s/BASE_SEPOLIA_RPC=.*/BASE_SEPOLIA_RPC=$BASE_SEPOLIA_RPC/" .env
sed -i "s/OP_SEPOLIA_RPC=.*/OP_SEPOLIA_RPC=$OP_SEPOLIA_RPC/" .env

