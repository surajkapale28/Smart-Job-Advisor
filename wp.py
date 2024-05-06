import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("smartjobadvisor@gmail.com", "xgvl qgvp qdsh eleh")

# message to be sent
message = "Your Resume has been selected"

# sending the mail
s.sendmail("smartjobadvisor@gmail.com", "surajkapale28@gmail.com", message)

# terminating the session
s.quit()
