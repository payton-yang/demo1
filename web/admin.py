from django.contrib import admin
from .models import Feedback


# Register your models here.
@admin.register(Feedback)
class AdminExample(admin.ModelAdmin):
    pass
