# Generated by Django 3.2.7 on 2021-09-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_question_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
