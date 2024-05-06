import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromEmail = 'smartjobadvisor@gmail.com'
fromEmailPassword = 'hgsh mtit vrhs gezh'


def sendEmail(course_list,e_mail,act_name):
    toEmail = e_mail
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Job  Recommendations'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'JOb Recommended'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    # Create a text version of the email
    text_content = f'''Hello {act_name} ..... Here are some job reccomendations you might find interesting:\n\n'''
    for course in course_list:
        text_content += f'- {course[0]} ({course[1]})\n'

    msgText = MIMEText(text_content)
    msgAlternative.attach(msgText)

    # Create an HTML version of the email with links
    html_content = f'<p>Dear {act_name}....Here are Job Reccomendations you might find interesting:</p><ul>'
    for course in course_list:
        html_content += f'<li><a href="{course[1]}">{course[0]}</a></li>'
    html_content += '</ul>'

    msgText = MIMEText(html_content, 'html')
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()
