# Generated by Django 2.2.5 on 2019-11-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20191125_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
