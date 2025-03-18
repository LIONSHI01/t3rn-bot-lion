# network_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

networks = {
    'Base': {
        'rpc_url': 'https://sepolia.base.org',
        'chain_id': 84532,
        'contract_address': '0x9D5cfa02e19dd0c3B05eCd1a3d9cf537FEE847d0'
    },
    'OP Sepolia': {
        'rpc_url': 'https://endpoints.omniatech.io/v1/op/sepolia/public',
        'chain_id': 11155420,
        'contract_address': '0xACa2218Fa847aECfe174fD1da80a90B7B3Ce4E17'
    },
}
