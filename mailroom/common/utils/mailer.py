from smtplib import SMTP_SSL
from email.message import EmailMessage

from .decorators import suppress_exceptions

"""
Mailer functions - for sending out
messages to the respective mailboxes
"""

@suppress_exceptions(False)
def send_mail(smtp_credentials, recipient, subject, message):
    """
    Sends the message via the designated SMTP server
    Returns true if successful, else False (or execeptions!)
    """
    msg_object = EmailMessage()
    msg_object['Subject'] = subject
    msg_object['From'] = smtp_credentials['sender']
    msg_object['To'] = recipient
    msg_object.set_content(message)

    with SMTP_SSL(smtp_credentials['host']) as smtp:
        if smtp_credentials.get('username', None) is not None:
            smtp.login(smtp_credentials['username'], smtp_credentials['password'])
        smtp.send_message(msg_object)

    return True
