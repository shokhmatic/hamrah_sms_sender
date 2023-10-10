import logging

from logging import config

log_config = {
    "version": 1,
    "root": {"handlers": ["console"], "level": "DEBUG"},
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        }
    },
    "formatters": {
        "std_out": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
            "datefmt": "%d-%m-%Y %I:%M:%S",
        }
    },
}

config.dictConfig(log_config)
