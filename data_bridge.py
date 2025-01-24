import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


data_bridge = {
    # Data bridge Base
    "Base - OP Sepolia": os.getenv('DATA_BRIDGE_BASE_TO_OP'),

    # Data bridge OP Sepolia
    "OP - Base": os.getenv('DATA_BRIDGE_OP_TO_BASE'),
}
