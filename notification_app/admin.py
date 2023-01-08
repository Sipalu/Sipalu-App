from django.contrib import admin

# Admin for notification.
from .models import BroadcastNotification
admin.site.register(BroadcastNotification)