#!/usr/local/bin/python

import json
from include import hCheckhost
from include import hLogger


def main():
    logger = hLogger.initLog()
    logger.info("[INFO] service port check #############")

    try:
        with open('./config.json', encoding='utf-8') as f:
            json_object = json.load(f)
            checkArray = json_object['service']
            emailConfig = json_object['config']
            emailList = json_object['address']
            hCheckhost.serverCheck(checkArray, emailConfig, emailList)
    except FileNotFoundError as e:
        logger.info(e)

    logger.info("[INFO] service port check done ########")


if __name__ == "__main__":
    main()
