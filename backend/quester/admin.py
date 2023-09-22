from django.contrib import admin
from .models import Quester

# Register your models here.
class QuesterAdmin(admin.ModelAdmin):
    list_display= ("title", "description", "completed", "level")


admin.site.register(Quester, QuesterAdmin)