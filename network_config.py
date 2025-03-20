# network_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

networks = {
    'Base': {
        'rpc_url': os.getenv('BASE_SEPOLIA_RPC'),
        'chain_id': 84532,
        'contract_address': '0xCEE0372632a37Ba4d0499D1E2116eCff3A17d3C3'
    },
    'OP Sepolia': {
        'rpc_url': os.getenv('OP_SEPOLIA_RPC'),
        'chain_id': 11155420,
        'contract_address': '0xb6Def636914Ae60173d9007E732684a9eEDEF26E'
    },
}
