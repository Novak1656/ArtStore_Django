# Generated by Django 4.0.5 on 2022-07-29 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import galery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ImageField(upload_to=galery.models.get_art_url, verbose_name='Арт')),
                ('art_title', models.CharField(max_length=250, verbose_name='Название')),
                ('genre', models.CharField(max_length=150, verbose_name='Жанр')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('art', models.ImageField(upload_to=galery.models.get_art_url, verbose_name='Арт')),
                ('create_on', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('update_on', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('prise', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Стоимость')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art', to='galery.genre')),
            ],
        ),
    ]