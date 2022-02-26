import json

from django.core import serializers
from django.core.mail import EmailMultiAlternatives, send_mail
from django.dispatch import receiver
from django.forms import model_to_dict
from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


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
    context = {
        "current_user": serializers.serialize("json", [reset_password_token.user]),
        "username": reset_password_token.user.username,
        "email": reset_password_token.user.email,
        "reset_password_url": "{}?token={}".format(
            instance.request.build_absolute_uri(
                reverse("password_reset:reset-password-confirm")
            ),
            reset_password_token.key,
        ),
    }

    if reset_password_token.user.last_login:
        subject = "Reset password"
        email_html_message = render_to_string("email/user_reset_password.html", context)
    else:
        subject = "[leiracon] Confirm your email"
        email_html_message = render_to_string("email/email_confirmation.html", context)

    # render email text

    # email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        subject,
        body=email_html_message,
        from_email="admin@leiriacon.pt",
        to=[reset_password_token.user.email],
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
