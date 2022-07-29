from django.db import models
from authentication.models import User


def get_art_url(instance, filename):
    return f"img/arts/shop_arts/{instance.author.username}/{filename}"


class Genre(models.Model):
    title = models.CharField('Название', max_length=250)

    def __str__(self):
        return self.title


class Art(models.Model):
    title = models.CharField('Название', max_length=250)
    art = models.ImageField('Арт', upload_to=get_art_url)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='art')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='art')
    create_on = models.DateTimeField('Время добавления', auto_now_add=True)
    update_on = models.DateTimeField('Время изменения', auto_now=True)
    prise = models.DecimalField('Стоимость', max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_on']


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery')
    art = models.ImageField('Арт', upload_to=get_art_url)
    art_title = models.CharField('Название', max_length=250)
    genre = models.CharField('Жанр', max_length=150)
    author = models.CharField('Автор', max_length=150)
    created_on = models.DateTimeField('Время добавления', auto_now_add=True)

    def __str__(self):
        return self.art.name

    class Meta:
        ordering = ['-created_on']
