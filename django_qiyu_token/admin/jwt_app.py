from django.contrib import admin

from django_qiyu_token.models import JwtAppModel


@admin.register(JwtAppModel)
class JwtAppAdmin(admin.ModelAdmin):
    list_display = ("app_name", "app_type", "ctime")
    list_display_links = ("app_name", "app_type")
    list_filter = ("app_name",)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return "ctime"
        else:
            return "ctime", "app_key"
