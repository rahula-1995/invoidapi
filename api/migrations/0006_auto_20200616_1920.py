# Generated by Django 2.2.7 on 2020-06-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200616_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseapi',
            name='base64',
            field=models.TextField(default='none', max_length=20000),
        ),
    ]
