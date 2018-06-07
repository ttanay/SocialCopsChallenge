from django.core.mail import send_mail

from . import models

from datetime import datetime
import requests

from challenge.credentials import MSG91_URL

def send_email(user):
    send_mail(
        "Your name is {}".format(user.name),
        "Hello! your name is {}. \n\nCheers!\nT. Tanay".format(user.name),
        "ttanay100@gmail.com",
        [user.email],
        fail_silently=False,
    )
    return

def email_helper(user, fail_count=0):
    if fail_count > 4:
        return
    try:
        send_email(user)
    except Exception as e:
        now = datetime.now()
        now = now.strftime("%d %b %Y, %H:%M")
        failure_message = "<u>{} Mail: </u> {}<br>".format(now, e)
        user.service_failure += failure_message
        fail_count += 1
        email_helper(user, fail_count)
    return

def phone_helper(user, fail_count=0):
    if fail_count > 4:
        return
    try:
        r = requests.get(MSG91_URL.format(user.phone_number, user.name))
    except:
        now = datetime.now()
        now = now.strftime("%d %b %Y, %H:%M")
        failure_message = "<u>{} SMS: </u> {}<br>".format(now, e)
        user.service_failure += failure_message
        fail_count += 1
        phone_helper(user, fail_count)
    return

#CRONJOBS

def mail_service():
    target_users = models.CustomUser.objects.all().exclude(email_activation_timestamp__isnull=True)
    for user in target_users:
        email_helper(user)
    return

def phone_service():
    target_users = models.CustomUser.objects.all().exclude(email_activation_timestamp__isnull=True)
    for user in target_users:
        phone_helper(user)
    return
