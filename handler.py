import requests
import json
from config import logging

logger = logging.getLogger(__name__)


def send_sms(number: str) -> str:
    logger.info(f"number: {number} | processing")
    url = "https://ai.hamrah.academy/api/sendsms"

    """
    Only content-type is required in hamrah academy!
    WTF?!
    """
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Language': 'en-US,en;q=0.9',
        # 'Connection': 'keep-alive',
        "Content-Type": "application/json",
        # 'Cookie': ''
        # 'Origin': 'https://ai.hamrah.academy',
        # 'Referer': 'https://ai.hamrah.academy/?utm_source=telegram&utm_medium=social&utm_campaign=aipack&utm_ne=AI&utm_term=ai_itme_7&utm_content=ownedmedia',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        # 'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"Windows"'
    }
    payload = json.dumps({"mobile": number})
    response = requests.request("POST", url, headers=headers, data=payload)
    logger.info(f"number: {number} | processed!")
    logger.info(f"number: {number} | {response.text}")
    return response.text
