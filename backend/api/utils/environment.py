import os

_convention_name: str = "NAME"
_convention_logo: str = "LOGO_URL"
_app_url: str = "APP_URL"


def get_app_name():
    return os.environ.get(_convention_name, "")


def get_logo_url():
    return os.environ.get(_convention_logo, "")


def get_app_url():
    return f"{os.environ.get(_app_url, '')}"


def get_reset_password_url():
    return f"{get_app_url()}/new-password/?token="
