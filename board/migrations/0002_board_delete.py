# Generated by Django 2.2.2 on 2019-06-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
