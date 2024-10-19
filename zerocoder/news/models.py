from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
                               verbose_name='Автор')  # Replace 1 with the ID of the default user

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
