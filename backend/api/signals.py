import logging

from django.core import serializers
from django.core.mail import EmailMessage
from django.dispatch import Signal, receiver
from django.template.loader import get_template
from django_rest_passwordreset.signals import reset_password_token_created
from dotenv import find_dotenv, load_dotenv

from backend.api.utils import environment

load_dotenv(find_dotenv())  # loads the configs from .env
# reading .env file


user_created = Signal()


def send_mail_html(subject, body, to):
    msg = EmailMessage(
        subject,
        body=body,
        from_email="info@leiriacon.pt",
        to=to,
        reply_to=["info@spielportugal.org"],
    )
    msg.content_subtype = "html"
    msg.send()


def send_mail_with_url(data, subject: str, template: str):
    try:
        context = {
            "current_user": serializers.serialize("json", [data.user]),
            "user_first_name": data.user.first_name,
            "username": data.user.username,
            "email": data.user.email,
            "reset_password_url": f"{environment.get_reset_password_url()}{data.key}",
            "logo_url": environment.get_logo_url(),
            "name": environment.get_app_name(),
            "app_url": environment.get_app_url(),
        }

        send_mail_html(
            subject=subject,
            body=get_template(template).render(context),
            to=[data.user.email],
        )

    except Exception as err:
        logging.error(err)
        raise err


@receiver(reset_password_token_created)
def send_password_url_by_mail(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    logging.info("Received reset_password_token_created signal")
    send_mail_with_url(
        reset_password_token,
        subject=f"Reset your {environment.get_app_name()} password",
        template="email/password_reset.html",
    )


@receiver(user_created)
def send_password_url_by_mail_to_new_user(
    sender, instance, reset_password_token, *args, **kwargs
):

    # send an e-mail to the user
    logging.info("Received user_created signal")
    send_mail_with_url(
        reset_password_token,
        subject=f"Welcome to {environment.get_app_name()}'s portal",
        template="email/welcome.html",
    )
