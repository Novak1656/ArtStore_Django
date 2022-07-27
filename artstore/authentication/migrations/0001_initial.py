# Generated by Django 4.0.5 on 2022-07-27 18:27

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('roles', models.CharField(default='Пользователь', max_length=100, verbose_name='Статус')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('avatar', models.CharField(default='E:\\python_proj\\MainProjects\\DjangoProj\\ArtStore\\artstore\\authentication/static/img/avatar.jpg', max_length=250, verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]