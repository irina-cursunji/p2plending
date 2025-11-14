from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


from .models import User

from allauth.account.forms import SignupForm
from django.contrib.auth import forms as admin_forms
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User
from .models import Useraddress


if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.site.login = login_required(admin.site.login)  # type: ignore[method-assign]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    list_display = ('first_name' , 'last_name', 'country_of_residence', 'account_type')
    list_display_links = ('first_name' , 'last_name', 'country_of_residence', 'account_type')

@admin.register(Useraddress)
class UserAddresAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')

    list_display_links = ('user', 'address_line_1', 'address_line_2', 'state', 'city', 'zip_post_code', 'country')

