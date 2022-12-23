from home.models import *

def delete_notification(id: int) -> None:
    Notifications.objects.get(pk=id).delete()