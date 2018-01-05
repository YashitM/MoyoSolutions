from allauth.account.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

from website.models import CustomUser


@receiver(user_logged_in)
def user_logged_in_(request, user, **kwargs):
    # check if uid already exists in custom user table, if it does then dont update data, otherwise do
    print(user.id)
    print(user.socialaccount_set.all()[0].uid)
    # current_session_id = sociallogin.account.uid
    # all_users = CustomUser.objects.all()
    # user_already_exists = False
    # existing_user = None
    #
    # for user in all_users:
    #     if user.fb_id == current_session_id and not user.user_id:
    #         user_already_exists = True
    #         existing_user = user
    #         break
    #
    # if user_already_exists:
    #     print("User Already Exists")
    #     selected_user_id = existing_user.id
    #     complete_user = CustomUser.objects.get(pk=selected_user_id)
    #     complete_user.user_id = sociallogin.account.user_id
    #     complete_user.save()
