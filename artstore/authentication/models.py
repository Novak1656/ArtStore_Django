from django.db import models
from django.contrib.auth.models import AbstractUser


def get_avatar_url(instance, filename):
    return f"img/user_avatars/{instance.username}/{filename}"


class User(AbstractUser):
    roles = models.CharField('Статус', default='Пользователь', max_length=100)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to=get_avatar_url, blank=True)

    def __str__(self):
        return self.username
