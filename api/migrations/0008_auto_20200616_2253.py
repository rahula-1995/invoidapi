# Generated by Django 2.2.7 on 2020-06-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200616_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseapi',
            name='aes',
            field=models.TextField(default='none', max_length=10000),
        ),
        migrations.AlterField(
            model_name='responseapi',
            name='md5',
            field=models.TextField(default='none', max_length=5000),
        ),
    ]
