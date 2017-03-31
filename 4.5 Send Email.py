"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("youremailusername", "password")

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "target@example.com", msg)

#To include a From, To and Subject headers, we should use the email package,
#since smtplib does not modify the contents or headers at all.

#Python's email package contains many classes and functions for composing and
#parsing email messages.


#We start by only importing only the classes we need, this also saves us from
#having to use the full module name later.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Then we compose some of the basic message headers:

fromaddr = "you@gmail.com"
toaddr = "target@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

#Next, we attach the body of the email to the MIME message:

body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

#For sending the mail, we have to convert the object to a string, and then
#use the same prodecure as above to send using the SMTP server..

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("youremailusername", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

#Check email addres
#The SMTP protocol includes a command to ask a server whether an address is valid. 

# Usually VRFY is disabled to prevent spammers from finding legitimate email 
# addresses,but if it is enabled you can ask the server about an address and
# receive a status code indicating validity along with the user’s full name. 

# This example is based on this post




import smtplib

server = smtplib.SMTP('mail')
server.set_debuglevel(True)  # show communication with the server
try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()

print 'dhellmann:', dhellmann_result
print 'notthere :', notthere_result


import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
	
	
	
	
