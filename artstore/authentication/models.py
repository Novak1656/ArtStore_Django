import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Users(User):
    roles = models.CharField('Статус', default='Пользователь', max_length=100)
    date_of_birth = models.DateField('Дата рождения', null=True)
    avatar = models.CharField('Аватар', max_length=250,
                              default=os.path.join(settings.BASE_DIR,
                                                   'authentication/static/img/avatar.jpg'))
