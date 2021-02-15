#!/usr/local/bin/python

import logging
from include import hEmail
import socket
import time

logger = logging.getLogger('log')


def serverCheck(check, config, toEmail):
    logger.info("[INFO] serverCheck() start...")
    msg_top = "# 서비스 포트 점검  \n"
    msg_top = msg_top + ">서비스 체크에 실패하였을 때 발송하는 메일입니다.  \n"
    msg_top = msg_top + ">메일 수신 즉시 내용에 대해 조치하시기 바랍니다.  \n"
    msg_top = msg_top + "  \n"
    msg_top = msg_top + " - " + checkIp() + "에서 각 항목의 포트 연결여부를 점검 합니다.\n"
    delay = config['delay']
    msg_top = msg_top + " - 항목 당 " + str(delay) + "번 재시도 하였습니다.\n"

    msg_contents = "# 서비스 포트 점검 리스트\n"
    failCnt = 0

    for arr in check:

        name = arr['name']
        ip = arr['ip']
        port = arr['port']

        tmp = checkHost(ip, port, config)
        logger.info("[INFO] {0} service ({1}:{2}) = {3}".format(name, ip, port, tmp))

        if not tmp:
            msg_contents = msg_contents + " - {0} service ({1}:{2}) = " \
                                          "<span style=\"color:red; font-weight:bold\">{3}</span>".format(name, ip,
                                                                                                          port,
                                                                                                          tmp) + "\n"
            failCnt = failCnt + 1
        else:
            msg_contents = msg_contents + " - {0} service ({1}:{2}) = {3}".format(name, ip, port, tmp) + "\n"

    if failCnt > 0:
        msg_top = msg_top + ' - 전체 <span style=\"font-size: large; font-weight:bold\">' \
                  + str(len(check)) \
                  + '</span>개 서비스 중 <span style=\"color:red; font-size: large; font-weight:bold\">' \
                  + str(failCnt) \
                  + '</span>개가 오류 입니다.\n'
        msg = msg_top + msg_contents
        hEmail.sendEmail(config, toEmail, msg)
    else:
        logger.info('[INFO] 모든 서비스 정상 동작 합니다.')

    logger.info("[INFO] serverCheck() end...")


def isOpen(ip, port, config):
    timeout = config['timeout']
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except socket.error as e:
        logger.info("[EXCEPT] " + str(ip) + ":" + str(port) + " = " + str(e))
        return False
    finally:
        s.close()


def checkHost(ip, port, config):
    result = False
    retry = config['retry']
    delay = config['delay']

    for i in range(retry):
        if isOpen(ip, port, config):
            result = True
            break
        else:
            time.sleep(delay)
    return result


def checkIp():
    return socket.gethostbyname(socket.getfqdn())
