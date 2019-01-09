from django.contrib import admin

from .models import BlockedEmail, BlockedIp, BlockedWord
# Register your models here.
admin.site.register(BlockedEmail)
admin.site.register(BlockedIp)
admin.site.register(BlockedWord)
