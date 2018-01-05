from allauth.account.signals import user_logged_in
from django.dispatch import receiver

from website.models import CustomUser


@receiver(user_logged_in)
def user_logged_in_(request, user, **kwargs):
    all_users = CustomUser.objects.all()
    user_already_exists = False
    existing_user = None

    for current_user in all_users:
        if current_user.fb_id == user.socialaccount_set.all()[0].uid:
            user_already_exists = True
            existing_user = current_user
            break

    if user_already_exists:
        if not existing_user.user_id:
            existing_user.user_id = user.id
            existing_user.save()
    else:
        new_user = CustomUser()
        new_user.fb_id = user.socialaccount_set.all()[0].uid
        new_user.name = user.first_name + " " + user.last_name
        new_user.email = user.email
        new_user.created_at = user.date_joined
        new_user.user_id = user.id
        new_user.save()


