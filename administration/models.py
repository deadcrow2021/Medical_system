from django.db import models


# Create your models here.
class Files(models.Model):
    title = models.CharField('Название документа', max_length=200, unique=True)
    description = models.CharField('Описание', max_length=200, blank=True)
    upload_date = models.DateField('Дата загрузки', auto_now_add=True)
    document = models.FileField('Документ', upload_to='uploads/')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['upload_date']

class ClinicRecomendations(models.Model):
    title = models.CharField('Название документа', max_length=200, unique=True)
    document = models.FileField('Документ', upload_to='uploads/')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Клиническая рекомендация'
        verbose_name_plural = 'Клинические рекомендации'
