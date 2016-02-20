# ====================================================================
#       This will send a email with a picture mixed in the text.
# ====================================================================

from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import smtplib

from_addr = "junkuizhang@126.com"
to_addr = "364772080@qq.com"

pwd = "ZJKzhangjunkui01"
smtpurl = "smtp.126.com"

msg = MIMEMultipart()

# message = MIMEText("<html><body><h1>Hello, see the picture?</h1><p><img src='cid:0'></p></body></html>", "html", "utf-8")

# The above assignment will cause a data error "554:DT SPAM", says it's not allowed to send the email with a picture
# mixed in the text. URL HERE: http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html

message = MIMEText("<html><body><h1>Hello, see the picture?</h1></body></html>", "html", "utf-8")

def getFormatAddr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, "utf-8").encode(), addr))

msg["From"] = getFormatAddr("Junkui Zhang <%s>" % from_addr)
msg["To"] = getFormatAddr("Me <%s>" % to_addr)
msg["Subject"] = Header("Picture in the text.", "utf-8").encode()
msg.attach(message)

with open("0.jpg", "rb") as fi:
	pic = MIMEBase("image", "jpg", filename="0.jpg")
	pic.add_header("Content-Disposition", "attachment", filename="0.jpg")
	pic.add_header("Content-ID", "<0>")
	pic.add_header("X-Attachment-ID", "0")
	pic.set_payload(fi.read())
	encode_base64(pic)
	msg.attach(pic)

sever = smtplib.SMTP(smtpurl, 25)
sever.login(from_addr, pwd)
sever.sendmail(from_addr, [to_addr], msg.as_bytes())
sever.close()
print("Done")