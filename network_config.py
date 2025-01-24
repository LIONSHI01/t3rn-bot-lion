# network_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

networks = {
    'Base': {
        'rpc_url': os.getenv('BASE_SEPOLIA_RPC'),
        'chain_id': 84532,
        'contract_address':
        '0x30A0155082629940d4bd9Cd41D6EF90876a0F1b5'
    },
    'OP Sepolia': {
        'rpc_url': os.getenv('OP_SEPOLIA_RPC'),
        'chain_id': 11155420,
        'contract_address': '0xF221750e52aA080835d2957F2Eed0d5d7dDD8C38'
    },
}
