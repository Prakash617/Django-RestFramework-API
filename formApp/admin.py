from django.contrib import admin
from .models import addStd

@admin.register(addStd)
class addStdAdmin(admin.ModelAdmin):
    list_display=('stdId','stdName','stdEmail','stdPassword')