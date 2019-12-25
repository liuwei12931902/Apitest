import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from Config import GlobalConfig
from public.Common.ReadConfigini import ReadConfigini


# [email]
# mail_server = smtp.qq.com
# sender_qq = 1341727538@qq.com
# pwd = qq授权码
# receiver = 401113727@qq.com

# 调用ReadConfig读取配置文件
config_path = GlobalConfig.configIni_path
ReadConfig = ReadConfigini(config_path).getConfigValue


def sendReportFile(file_path):
    host_server = ReadConfig('email', 'mail_server')
    sender_qq = ReadConfig('email', 'sender_qq')
    pwd = ReadConfig('email', 'pwd')
    receiver = ReadConfig('email', 'receiver')
    # 读取路径
    sendfile = open(file_path, 'rb').read()
    msg = MIMEText(sendfile, _subtype='html', _charset='utf-8')
    msg['Content-Type'] = 'application/octet-stream'
    msg['Content-Disposition'] = 'attachment; filename = result.html'

    msgRoot = MIMEMultipart('related')
    # msgtext = MIMEText(content, _subtype='plain', _charset='utf-8')
    msgRoot.as_string(msg)

    msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
    msg['From'] = sender_qq
    msg['To'] = receiver

    smtp = smtplib.SMTP(host_server)
    smtp.set_debuglevel(1)
    smtp.login(sender_qq, pwd)
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out')


def newReport(testReport):
    lists = os.listdir(testReport)
    lists2 = lists.sort(reverse=True)
    return os.path.join(testReport, lists[0])


if __name__ == '__main__':
    f = newReport(GlobalConfig.report_path)
    print(f)
    sendReportFile(f)
