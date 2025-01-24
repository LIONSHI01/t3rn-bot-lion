# keys_and_addresses.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 私钥列表 (每个私钥应为一个字符串)
private_keys = [
    os.getenv('PRIVATE_KEY'),
]

labels = [
    os.getenv('LABEL'),
]
