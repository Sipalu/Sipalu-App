<<<<<<< HEAD
from notification_app.models import BroadcastNotification


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()

    return {'notifications': allnotifications}
=======
from notification_app.models import BroadcastNotification


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()

    return {'notifications': allnotifications}
>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9
