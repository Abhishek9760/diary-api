from django.contrib import admin

from .models import Diary
from .forms import DiaryForm


class DiaryAdmin(admin.ModelAdmin):
    list_display = ["user", "__str__", "image"]
    form = DiaryForm


admin.site.register(Diary, DiaryAdmin)
