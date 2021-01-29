import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "935037060@qq.com"
toaddr = "935037060@qq.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
# 邮件主题
msg['Subject'] = "Hooah"
# 邮件正文
body = "HAHAHA!"

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP("smtp.qq.com")
server.starttls()
server.login(fromaddr, "xindekaishi2019")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()