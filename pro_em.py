# Python code to illustrate Sending mail with attachments
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("vinayak16101999@gmail.com","qwertyuiop")
message ="hello"
s.sendmail("vinayak16101999@gmail.com","vikramv7654@gmail.com",message)
print("success")
s.quit()
