from setting import logger
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import setting


def send_mail(message, receiver=setting.receiver):
    logger.info('start sending')
    sender = setting.sender
    password = setting.password
    smtp_server = setting.smtp_server
    try:
        content = '登陆验证码 %s' % message
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["Server", sender])
        msg['To'] = formataddr(["engineer", receiver])
        msg['Subject'] = "验证码"  # title

        server = smtplib.SMTP(smtp_server, 25)
        server.login(sender, password)
        server.sendmail(sender, [
            receiver,
        ], msg.as_string())
        server.quit()
        logger.info('success send')
    except Exception as err:
        logger.error(err)


if __name__ == '__main__':
    message = '123456'
    receiver = 'xx.@xx.com'
    sender(message, receiver)
