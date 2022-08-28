from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(pre_save, sender=CustomUser)
def post_save_create_profile(sender, instance, **kwargs):
    if instance.password == '':
        instance.password = 'Zxzxzxzx13579'