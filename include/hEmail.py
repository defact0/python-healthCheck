#!/usr/local/bin/python

import markdownmail
import logging

logger = logging.getLogger('log')


def sendEmail(config, toEmail, message):
    logger.info("[INFO] sendEmail() start...")

    email = markdownmail.MarkdownMail(
        from_addr=config['id'],
        to_addr=toEmail,
        subject=config['title'],
        content=message
    )
    email.send("smtp.gmail.com", port=587, login=config['id'], password=config['pw'], tls=True)

    logger.info("[INFO] sendEmail() end...")
