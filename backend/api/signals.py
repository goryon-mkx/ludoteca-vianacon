import logging
import os

from django.core import serializers
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string, get_template
from django_rest_passwordreset.signals import reset_password_token_created


from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # loads the configs from .env
# reading .env file


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
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
    try:
        context = {
            "current_user": serializers.serialize("json", [reset_password_token.user]),
            "username": reset_password_token.user.username,
            "email": reset_password_token.user.email,
            "reset_password_url": f"{os.environ.get('EMAIL_TEMPLATE_BASE_URL')}?token={reset_password_token.key}",
        }

        subject = "leiriacon.pt - Reset your password"
        body = get_template("email/password_reset.html").render(context)

        msg = EmailMessage(
            subject,
            body=body,
            from_email="info@leiriacon.pt",
            to=[reset_password_token.user.email],
            reply_to=['info@spielportugal.org']
        )
        msg.content_subtype = "html"
        msg.send()

    except Exception as err:
        logging.error(err)
        raise err
