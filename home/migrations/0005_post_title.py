# Generated by Django 3.2.20 on 2024-01-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='empty', max_length=50),
        ),
    ]
