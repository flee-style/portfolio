# Generated by Django 2.2.5 on 2019-11-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]