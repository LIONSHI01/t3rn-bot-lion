#!/bin/bash

read -p "Number of ETH to Bridge:" BRIDGE_AMOUNT
read -p "Data from Base to OP:" DATA_BRIDGE_BASE_TO_OP
read -p "Data from OP to Base:" DATA_BRIDGE_OP_TO_BASE

sed -i "s/BRIDGE_AMOUNT=.*/BRIDGE_AMOUNT=$BRIDGE_AMOUNT/" .env
sed -i "s/DATA_BRIDGE_BASE_TO_OP=.*/DATA_BRIDGE_BASE_TO_OP=$DATA_BRIDGE_BASE_TO_OP/" .env
sed -i "s/DATA_BRIDGE_OP_TO_BASE=.*/DATA_BRIDGE_OP_TO_BASE=$DATA_BRIDGE_OP_TO_BASE/" .env

