# Generated by Django 2.2.7 on 2020-06-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='api/images')),
                ('basestring', models.CharField(default='none', max_length=50)),
                ('md5', models.CharField(default='none', max_length=50)),
            ],
        ),
    ]
