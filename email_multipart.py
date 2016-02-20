from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

from_addr = "junkuizhang@126.com"
to_addr = "364772080@qq.com"

pwd = "ZJKzhangjunkui01"
smtp_sever = "smtp.126.com"

msg = MIMEMultipart()
text = MIMEText("Tell me what're the strings in the picture.", "plain", "utf-8")

def getFormatAddr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, "utf-8").encode(), addr))

msg["From"] = getFormatAddr("Junkui Zhang <%s>" % from_addr)
msg["To"] = getFormatAddr("me <%s>" % to_addr)
msg["Subject"] = Header("This is a message from SMTP!", "utf-8").encode()

msg.attach(text)

with open("0.jpg", "rb") as fi:
	pic = MIMEBase("image", "jpg", filename="0.jpg")
	pic.add_header("Content-Disposition", "attachment", filename="0.jpg")
	pic.add_header("Content-ID", "<0>")
	pic.add_header("X-Attachment-ID", "0")
	pic.set_payload(fi.read())
	encoders.encode_base64(pic)
	msg.attach(pic)

sever = smtplib.SMTP(smtp_sever, 25)
sever.login(from_addr, pwd)
sever.sendmail(from_addr, [to_addr], msg.as_string())
sever.close()
print("Done.")