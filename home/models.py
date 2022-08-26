from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("Имя", max_length=15)
    password = models.CharField("Пароль", max_length=10)
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"