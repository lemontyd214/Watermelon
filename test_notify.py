import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "dota2daily"  # 用户名
mail_pass = "IMXEZHFKBGMLNFCW"  # 口令

sender = 'dota2daily@163.com'
receivers = '931770556@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = sender
message['To'] = receivers[0]

subject = 'dota2daily 上传结果通知'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)
