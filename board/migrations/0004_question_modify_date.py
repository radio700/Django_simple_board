# Generated by Django 3.2.7 on 2021-09-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]