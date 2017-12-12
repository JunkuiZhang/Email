import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header

message = MIMEText("Hello world!", "plain", "utf-8")
from_addr = "junkuizhang@126.com"
pwd = "***"
to_addr = "364772080@qq.com"
smtp_sever = "smtp.126.com"

def getFormatAddr(data):
	name, addr = parseaddr(data)
	return formataddr((Header(name, "utf-8").encode(), addr))

message["From"] = getFormatAddr("Junkui Zhang <%s>" % from_addr)
message["To"] = getFormatAddr("This test <%s>" % to_addr)          # send to mutiple addresses, just use "," to distinguish them.
message["Subject"] = Header("This is a message from a Python programer", "utf-8").encode()

sever = smtplib.SMTP(smtp_sever, 25)
sever.login(from_addr, pwd)
sever.sendmail(from_addr, [to_addr], message.as_string())    # the [to_addr] is a list. Send to other recivers by adding elements.
sever.quit()
