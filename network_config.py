# network_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

networks = {
    'Base': {
        'rpc_url': 'https://base-sepolia.g.alchemy.com/v2/skX10ZnJcmh7VX25ejnqJw9ZRJekUIl0',
        'chain_id': 84532,
        'contract_address': '0xCEE0372632a37Ba4d0499D1E2116eCff3A17d3C3'
    },
    'OP Sepolia': {
        'rpc_url': 'https://opt-sepolia.g.alchemy.com/v2/skX10ZnJcmh7VX25ejnqJw9ZRJekUIl0',
        'chain_id': 11155420,
        'contract_address': '0xb6Def636914Ae60173d9007E732684a9eEDEF26E'
    },
}
