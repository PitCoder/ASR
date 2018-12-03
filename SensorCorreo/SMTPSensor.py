import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

smtpserver_ip_address = "10.100.79.162"
username = "pit@mailserver.asr"
destination = "jl@mailserver.asr"
password = "123456"

server = smtplib.SMTP(smtpserver_ip_address, 25)

start = time.time()

#Next, log in to the server
server.login(username, password)

#Assembling a email basic header
fromaddr = username
toaddr = destination
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Email"

#Now we attach the body of the email to the MIME message
body = "Configuration Administrator test email"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

end = time.time()

print("SMTP response time took (%.8f seconds passed)" % (end - start))

