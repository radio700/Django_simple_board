# Generated by Django 3.2.7 on 2021-11-05 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0007_auto_20211001_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='devoter',
            field=models.ManyToManyField(related_name='devoter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
