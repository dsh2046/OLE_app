import string
import random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from OLE.settings import EMAIL_FROM


def random_str(num):
    str = ''
    for x in range(num):
        str += random.choice(string.ascii_letters + string.digits)
    return str

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = 'OLE register URL'
        email_body = "Please click the URL below to activate your account: http://13.58.8.245:9000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = 'OLE password reset'
        email_body = 'Please click the URL below to reset your password: http://13.58.8.245:9000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update':
        email_title = 'Password update'
        email_body = 'Your Email verified code: {0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

