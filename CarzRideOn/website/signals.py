from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver


@receiver(pre_social_login)
def pre_social_login_(request, sociallogin, **kwargs):
    # check if uid already exists in custom user table, if it does then dont update data, otherwise do
    print(sociallogin.account.uid)
