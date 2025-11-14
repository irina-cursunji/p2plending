from django.contrib import admin

# Register your models here.

from .models import KycApplication, KycSetting


@admin.register(KycApplication)
class KycApplicationAdmin(admin.ModelAdmin):
    pass

@admin.register(KycSetting)
class KycSettingAdmin(admin.ModelAdmin):
    pass
