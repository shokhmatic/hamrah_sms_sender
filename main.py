import sys
from handler import send_sms
from config import logging

logger = logging.getLogger(__name__)


def run() -> None:
    list_of_arguments = sys.argv
    if len(list_of_arguments) < 2:
        logger.info("number is required")
        return
    number = list_of_arguments[1]
    logger.info(f"number: {number} | preprocessed")
    send_sms(number)


if __name__ == "__main__":
    run()
